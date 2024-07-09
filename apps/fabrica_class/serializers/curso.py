from rest_framework import serializers
from apps.fabrica_class.models import Curso

class CursoSerializer(serializers.ModelSerializer):
    turno = serializers.CharField(source='get_TurnoCurso_display')
    curso = serializers.CharField(source='get_TipoCurso_display')

    class Meta:
        model = Curso
        fields = ['id', 'nome', 'turno', 'curso']