from django.db import models
from FabricaClass.models import Formulario

class Pergunta(models.Model):
    descricao = models.CharField(max_length=255, default="Pergunta", null=True)
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, blank=True, null=True, unique=False)
    

    def __str__(self): 
        return self.descricao