from django.db import models
from apps.fabrica_class.models import Formulario

class Respostas(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    resposta = models.CharField(max_length=255)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    pergunta = models.ForeignKey("Pergunta", on_delete=models.CASCADE, blank=True, null=True, unique=False)

    def __str__(self):
        return self.resposta