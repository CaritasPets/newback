from django.db import models
from users.models import User
from django.conf import settings

class PetPerdido(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    especie = models.CharField(max_length=50, null=False, blank=False)
    genero = models.CharField(max_length=5, null=False, blank=False)
    localidade = models.CharField(max_length=200, null=False, blank=False)
    caracteristicas = models.TextField()
    foto = models.ImageField(upload_to='images/perdidos/', null=False, blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="pets_perdidos"
    )
    
    favoritos = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="favoritos_perdido",
        blank=True,
    )

    def __str__(self):
        return f"{self.nome} ({self.genero})"