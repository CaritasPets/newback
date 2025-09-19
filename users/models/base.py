from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    tipo = models.CharField(max_length=20, choices=(
        ('comum', 'Comum'),
        ('organization', 'Organization')
    ))
    #foto = models.ImageField(upload_to='images/', null=True)
