from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Espacos(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(max_length=1000)
    capacidade = models.IntegerField(default=0)

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

class Chamado(models.Model):
    STATUS= (
        ('abt', 'ABERTO'),
        ('and', 'EM ANDAMENTO'),
        ('ccl', 'CONCLUIDO'),
        )
    solicitante = models.CharField(max_length=255)
    data = models.DateField(auto_now_add=True)
    ambiente = models.ForeignKey(Espacos, on_delete=models.CASCADE)
    objeto = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=3, choices=STATUS, default='abt')

    def __str__(self):
        return self.solicitante