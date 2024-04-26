from rest_framework.viewsets import ModelViewSet
from FabricaClass.models import Formulario
from FabricaClass.serializers.formulario import FormularioListSerializer, FormularioWriteSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Formulario"])
class FormularioViewSet(ModelViewSet):
    queryset = Formulario.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list"]:
            return FormularioListSerializer
        return FormularioWriteSerializer


