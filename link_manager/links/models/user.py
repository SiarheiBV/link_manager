from django.contrib.auth.models import AbstractUser
from django.db import models

from .base import Base


class CustomUser(AbstractUser, Base):
    email = models.EmailField(max_length=35, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = "custom_user"
