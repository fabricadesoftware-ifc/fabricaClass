from rest_framework.routers import DefaultRouter
from apps.usuario import views

app_name = "apps.usuario"
router = DefaultRouter()
router.register("usuarios", views.UsuarioViewSet)



