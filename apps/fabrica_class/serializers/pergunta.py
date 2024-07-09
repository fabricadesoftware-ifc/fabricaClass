from rest_framework.serializers import ModelSerializer
from apps.fabrica_class.models import Pergunta

class PerguntaSerializer(ModelSerializer):
    class Meta:
        model = Pergunta
        fields: list[str] = [
            'id',
            'descricao',
            'criterio'
        ]