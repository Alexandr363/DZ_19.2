from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар',
                               blank=True, null=True)
    phone = models.CharField(max_length=35, verbose_name='телефон',
                             null=True, blank=True)
    county = models.CharField(max_length=50, verbose_name='страна',
                              blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
