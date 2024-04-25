from django.db import models

class Pergunta(models.Model):
    descricao = models.CharField(max_length=255, default="Pergunta", null=True)
    criterio = models.ForeignKey("Criterios", on_delete=models.CASCADE, blank=True, null=True, unique=False)
    

