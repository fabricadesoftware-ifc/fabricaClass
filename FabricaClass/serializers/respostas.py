from rest_framework.serializers import ModelSerializer
from FabricaClass.models import Respostas

class RespostasSerializer(ModelSerializer):
    class Meta:
        model = Respostas
        fields: list[str] = [
            'id',
            'data_hora',
            'resposta',
            'formulario',
            'usuario'
        ]