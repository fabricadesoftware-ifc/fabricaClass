from rest_framework.viewsets import ModelViewSet
from apps.fabrica_class.models import  Turma
from apps.fabrica_class.serializers import TurmaSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Turma'])
class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']