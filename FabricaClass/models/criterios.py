from django.db import models
class Criterios(models.Model):
  descricao = models.CharField(max_length=255, default="Criterio", null=True)
  valor_maximo = models.IntegerField(default=5)
  valor_minimo = models.IntegerField(default=1)


  def __str__(self):
     return self.descricao