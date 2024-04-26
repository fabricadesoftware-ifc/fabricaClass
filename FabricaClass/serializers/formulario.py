from rest_framework.serializers import ModelSerializer
from FabricaClass.models import Formulario

class FormularioListSerializer(ModelSerializer):
    class Meta:
        model = Formulario
        fields: list[str] = [
            'id',
            'data_hora_limite',
            'data_inicio',
            'data_fim',
            'titulo',
        ]

class FormularioWriteSerializer(ModelSerializer):
    class Meta:
        model = Formulario
        fields: list[str] = [
            'data_hora_limite',
            'data_inicio',
            'data_fim',
            'titulo',
            'descricao',
            'usuario',
            'pergunta'
        ]
