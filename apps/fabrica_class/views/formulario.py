from rest_framework.viewsets import ModelViewSet
from apps.fabrica_class.models import Formulario
from apps.fabrica_class.serializers.formulario import FormularioListSerializer, FormularioWriteSerializer
from drf_spectacular.utils import extend_schema
from apps.fabrica_class.paginations import FormularioPagination


extend_schema(tags=['Formulario'])
class FormularioViewSet(ModelViewSet):
    queryset = Formulario.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    pagination_class = FormularioPagination
    
    def get_serializer_class(self):
        if self.action in ["list"]:
            return FormularioListSerializer
        return FormularioWriteSerializer


