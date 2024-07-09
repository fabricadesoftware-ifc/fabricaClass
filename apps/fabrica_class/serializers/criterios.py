from rest_framework.serializers import ModelSerializer
from apps.fabrica_class.models import Criterios

class CriteriosSerializer(ModelSerializer):
    class Meta:
        model = Criterios
        fields: list[str] = [
            'id',
            'descricao',
            'valor_maximo',
            'valor_minimo'
        ]