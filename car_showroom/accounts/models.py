from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import models as auth_models

from car_showroom.accounts.managers import AppUserManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'
    objects = AppUserManager()
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30

    LAST_NAME_MAX_LEN = 30

    AGE_MIN_VALUE = 18

    email = models.EmailField(
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
    )

    age = models.PositiveIntegerField(
        validators=(MinValueValidator(
            AGE_MIN_VALUE,
            message='You must be at least 18 years old!'),
        ),
        null=True,
        blank=True,
    )

    profile_picture = models.FileField(
        null=True,
        blank=True,
    )
