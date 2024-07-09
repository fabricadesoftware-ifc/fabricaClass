from rest_framework.viewsets import ModelViewSet
from apps.fabrica_class.models import Pergunta
from apps.fabrica_class.serializers import PerguntaSerializer
from drf_spectacular.utils import extend_schema

extend_schema(tags=['Perguntas'])
class PerguntaViewSet(ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']