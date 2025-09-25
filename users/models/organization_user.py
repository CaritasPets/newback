from .base import User
from django.db import models

class OrganizationUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='organization_profile'
    )
    telefone = models.CharField(max_length=11, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    endereco = models.CharField(max_length=150, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
