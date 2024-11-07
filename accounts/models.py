from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_username, validate_password


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[validate_username],
        error_messages={
            'unique': "このユーザー名は既に使用されています。",
        },
    )
    password = models.CharField(
        max_length=128,
        validators=[validate_password],
    )

    class Meta:
        verbose_name_plural = 'CustomUser'
