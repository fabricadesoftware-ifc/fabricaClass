from rest_framework.serializers import ModelSerializer
from apps.fabrica_class.models import Turma

class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields: list[str] = [         
            'id',
            'ano_letivo',
            'semestre_letivo',
            'legenda',
            'curso',
        ]