import asyncio
import pandas as pd

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from usuario.models import Usuario
from FabricaClass.use_cases.send_email import generate_pie_graph, send_graph_by_email


@authentication_classes([])
@permission_classes([AllowAny])
class EmailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        subject = request.POST.get("subject", "Nome do email")
        message = request.POST.get("message", "Conteúdo do email")
        recipient_list = ["lucasantonete@hotmail.com"]


        usuarios = Usuario.objects.all()
        if usuarios:
            tipo_usuario_list = [usuario.tipo_usuario for usuario in usuarios]
            df = pd.DataFrame(tipo_usuario_list, columns=['tipo_usuario'])
        else:
            return Response("Erro ao obter os dados", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        image = generate_pie_graph(df)
        resultado_envio = asyncio.run(send_graph_by_email(subject, message, recipient_list, image))

        if resultado_envio:
            return Response(data={'message': resultado_envio}, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': "Erro ao enviar email"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)