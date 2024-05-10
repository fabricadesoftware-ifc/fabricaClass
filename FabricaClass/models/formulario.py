from django.db import models
from django.utils import timezone

class Formulario(models.Model):
    data_hora_limite = models.DateTimeField(null=True, blank=True)
    data_inicio = models.DateTimeField(default=timezone.now)
    data_fim = models.DateTimeField(null=True, blank=True)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


