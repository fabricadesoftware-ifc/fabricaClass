from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from apps.fabrica_class.views import TurmaViewSet, CursoViewSet, FormularioViewSet, RespostasViewSet, CriteriosViewSet, PerguntaViewSet, EmailAPIView
from apps.usuario.router import router as usuario_router
from apps.usuario.utils import newPassword
from apps.usuario.utils import cadastro, login, newPassword
from apps.uploader.router import router as uploader_router
# from FabricaClass.utils.pieGraph import EmailAPIView
# from FabricaClass.utils.managerDataFrame import ManagerDataFrame

router = DefaultRouter()
router.register(r"turmas", TurmaViewSet)
router.register(r"cursos", CursoViewSet)
router.register(r"formularios", FormularioViewSet)
router.register(r"respostas", RespostasViewSet)
router.register(r"criterios", CriteriosViewSet)
router.register(r"perguntas", PerguntaViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('api/cadastro/', cadastro.create_user, name='create_user'),
    path('api/login/', login.get_user, name='get_user'),
    path('api/new-password/', newPassword.forget_password, name='forget_password'),
    path('api/email/', EmailAPIView.as_view(), name='enviar_email'),
    path("api/media/", include(uploader_router.urls)),
    # path('api/dataframe/', ManagerDataFrame.as_view(), name='dataframe'),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)