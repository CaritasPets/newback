from .base import User
from django.db import models

class CommonUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='common_profile'
    )
    nome = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=11, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.user.username
