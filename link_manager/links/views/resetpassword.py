from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.urls import reverse
from links.models import CustomUser, PasswordResetToken
from links.serializers import PasswordResetSerializer


class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = CustomUser.objects.filter(email=email).first()

            if user:
                reset_token = PasswordResetToken.objects.create(user=user)
                reset_url = request.build_absolute_uri(reverse('password-reset-confirm', kwargs={'token': reset_token.token}))

                send_mail(
                    'Password Reset',
                    f'Click on the following link to reset your password: {reset_url}',
                    'no-reply@example.com',
                    [email],
                )

            return Response({"message": "If the email is registered, you will receive a password reset email"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    def post(self, request, token):
        reset_token = PasswordResetToken.objects.filter(token=token).first()

        if not reset_token or reset_token.is_expired():
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)

        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if new_password != confirm_password:
            return Response({"error": "New passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)

        user = reset_token.user
        user.set_password(new_password)
        user.save()

        reset_token.delete()

        return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
