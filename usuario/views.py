from rest_framework.viewsets import ModelViewSet
from usuario.models import Usuario
from .serializer import UsuarioSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Usuario'])
class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer