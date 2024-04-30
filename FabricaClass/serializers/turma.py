from rest_framework.serializers import ModelSerializer
from FabricaClass.models import Turma

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