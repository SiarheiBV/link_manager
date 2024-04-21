from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import logging

logger = logging.getLogger(__name__)


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        logger.info(f"Attempting to authenticate user with email: {email}")

        user = authenticate(username=email, password=password)

        if user:
            logger.info(f"User {email} authenticated successfully.")
            refresh = RefreshToken.for_user(user)
            return Response(
                {"message": "Login successful",
                 "username": user.username,
                 "email": user.email,
                 "token": str(refresh.access_token)
                 },
                status=status.HTTP_200_OK,
            )

        else:
            logger.warning(f"Authentication failed for user with email: {email}")
            return Response(
                {"message": "Invalid email or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
