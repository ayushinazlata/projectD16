from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class OneTimeCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    code = models.CharField(verbose_name='код', max_length=6)
    
