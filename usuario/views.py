from rest_framework.viewsets import ModelViewSet
from usuario.models import Usuario
from .serializer import UsuarioSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny


@authentication_classes([])
@permission_classes([AllowAny])
@extend_schema(tags=['Usuario'])
class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer