from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from apps.usuario.models import Usuario
from apps.usuario.serializer import UsuarioSerializer




@authentication_classes([])
@permission_classes([AllowAny])
@extend_schema(tags=['Usuario'])
class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer