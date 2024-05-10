from rest_framework.viewsets import ModelViewSet
from FabricaClass.models import Respostas
from FabricaClass.serializers import RespostasSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Respostas'])
class RespostasViewSet(ModelViewSet):
    queryset = Respostas.objects.all()
    serializer_class = RespostasSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']