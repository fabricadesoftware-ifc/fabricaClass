from rest_framework.viewsets import ModelViewSet
from FabricaClass.models import  Turma
from FabricaClass.serializers import TurmaSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Turma'])
class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']