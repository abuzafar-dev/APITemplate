from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import Task
from apps.serializers import TaskSerializer


class HealthCheckView(APIView):
    @extend_schema(responses=inline_serializer('Health', {'status': serializers.CharField()}))
    def get(self, request):
        return Response({'status': 'ok'})


class TaskViewSet(viewsets.ModelViewSet):
    """Vazifalar CRUD. ?is_done=true|false bilan filtrlash mumkin."""

    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        is_done = self.request.query_params.get('is_done')
        if is_done in ('true', 'false'):
            queryset = queryset.filter(is_done=is_done == 'true')
        return queryset
