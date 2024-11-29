from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.validators import AllNumbersValidator, TenCharactersValidator


class CustomUser(AbstractUser):
    phone = models.CharField(unique=True,
                             validators=[
                                 AllNumbersValidator(),
                                 TenCharactersValidator(),
                             ])

    preferred_address = models.CharField(
        max_length=100,
    )