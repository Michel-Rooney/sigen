from django.db import models
from django.contrib.auth.models import User

class Espacos(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(max_length=1000)

    imagem1 = models.ImageField(upload_to='fotos/espacos/imagem1', blank=True)
    imagem2 = models.ImageField(upload_to='fotos/espacos/imagem2', blank=True)
    imagem3 = models.ImageField(upload_to='fotos/espacos/imagem3', blank=True)
    imagem4 = models.ImageField(upload_to='fotos/espacos/imagem4', blank=True)
    imagem5 = models.ImageField(upload_to='fotos/espacos/imagem5', blank=True)

    def __str__(self):
        return self.nome


class NivelUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=3
    )
