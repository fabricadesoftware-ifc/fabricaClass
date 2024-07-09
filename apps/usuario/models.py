from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from apps.fabrica_class.models import Turma
from apps.usuario.managers import CustomUserManager
from apps.uploader.models import Image

class Usuario(AbstractUser):
    class TipoUsuario(models.IntegerChoices):
        PROFESSOR = (1, 'Professor',)
        ALUNO = (2, 'Aluno',)
    email = models.EmailField(_("e-mail address"), unique=True)
    username = models.CharField(_("Nome"), max_length=255, blank=True, null=True)
    matricula = models.CharField(_("Matricula/SIAPE"), max_length=11, blank=True, null=True)
    tipo_usuario = models.IntegerField(choices=TipoUsuario.choices,  default=TipoUsuario.ALUNO)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT, related_name='turma', blank=True, null=True)
    password_reset_token = models.CharField(
        _("Password Reset Token"), max_length=255, blank=True, null=True
    )
    password_reset_token_created = models.DateTimeField(
        _("Password Reset Token Created"), blank=True, null=True
    )  
    image_profile = models.ForeignKey(Image, on_delete=models.PROTECT, related_name='profile', blank=True, null=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]

