from rest_framework.viewsets import ModelViewSet
from apps.fabrica_class.models import Curso
from apps.fabrica_class.serializers import CursoSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Curso'])
class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']