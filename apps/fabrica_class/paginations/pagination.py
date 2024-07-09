from rest_framework import pagination
from apps.fabrica_class.models import Formulario
from core.settings import DEFAULT_LIMIT, LIMIT_QUERY_PARAM, OFFSET_QUERY_PARAM, MAX_LIMIT


class FormularioPagination(pagination.LimitOffsetPagination):
    default_limit = DEFAULT_LIMIT
    limit_query_param = LIMIT_QUERY_PARAM
    offset_query_param = OFFSET_QUERY_PARAM
    max_limit = MAX_LIMIT

    def get_limit(self, request):
        limit = super().get_limit(request)
        if limit is None:
            return len(Formulario.objects.all())
        return limit