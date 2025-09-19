from django.db import models

class PetPerdido(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    especie = models.CharField(max_length=50, null=False, blank=False)
    genero = models.CharField(max_length=5, null=False, blank=False)
    localidade = models.CharField(max_length=200, null=False, blank=False)
    caracteristicas = models.TextField()
    #foto = models.ImageField(upload_to='images/', null=False, blank=False)
    #dono = 
    
    def __str__(self):
        return f"{self.nome} ({self.genero})"