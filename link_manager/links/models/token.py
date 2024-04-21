import uuid
from django.db import models
from django.utils import timezone
from datetime import timedelta
from links.models import CustomUser


class PasswordResetToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reset_tokens')
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_in = models.DurationField(default=timedelta(hours=1))

    def is_expired(self):
        return timezone.now() > self.created_at + self.expires_in

    def __str__(self):
        return f'{self.user.email} - {self.token}'
