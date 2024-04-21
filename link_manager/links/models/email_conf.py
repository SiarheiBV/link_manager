from django.db import models
from .user import CustomUser
from .base import Base


class EmailConfirmationCodes(Base):
    user = models.ForeignKey(
        to=CustomUser, on_delete=models.CASCADE, related_name="codes"
    )
    code = models.CharField(max_length=100, unique=True)
    expiration = models.PositiveIntegerField()

    class Meta:
        db_table = "email_codes"
