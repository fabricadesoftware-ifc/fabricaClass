from rest_framework.serializers import ModelSerializer
from FabricaClass.models import Criterios

class CriteriosSerializer(ModelSerializer):
    class Meta:
        model = Criterios
        fields: list[str] = [
            'id',
            'descricao',
            'valor_maximo',
            'valor_minimo'
        ]