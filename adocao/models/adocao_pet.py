from django.db import models
from users.models import User

class PetAdocao(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    especie = models.CharField(max_length=50, null=False, blank=False)
    genero = models.CharField(max_length=5, null=False, blank=False)
    porte = models.CharField(max_length=7, null=False, blank=False)
    castrado = models.CharField(max_length=3, null=False, blank=False)
    raca = models.CharField(max_length=50, null=True, blank=True)
    vacinado = models.CharField(max_length=20, null=False, blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="pets_adocao"
    )
    #foto = models.ImageField(upload_to='images/', null=False, blank=False)
    

    def __str__(self):
        return f"{self.nome} ({self.especie})"
    