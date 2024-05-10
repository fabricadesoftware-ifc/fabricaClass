from rest_framework.viewsets import ModelViewSet
from FabricaClass.models import Criterios
from FabricaClass.serializers import CriteriosSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Criterios'])
class CriteriosViewSet(ModelViewSet):
    queryset = Criterios.objects.all()
    serializer_class = CriteriosSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']