from drf_spectacular.utils import extend_schema_view, extend_schema
from django.http import HttpRequest, HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from tasks.api.v1.serializers import (
    TaskSerializer,
    TaskUpdateSerializer,
    TaskCreateSerializer,
    TaskExecuteSerializer,
)
from tasks.models import Task
from tasks.services import TaskService
from utils.mixins import MethodMatchingViewSetMixin, ByUserCreatedMixin


@extend_schema_view(
    create=extend_schema(
        summary='Создать задачу',
        description='Создать задачу',
    ),
    list=extend_schema(
        summary='Получить список задач',
        description='Получить список задач',
    ),
    retrieve=extend_schema(
        summary='Получить задачу по ID',
        description='Получить задачу по ID',
    ),
    update=extend_schema(
        summary='Обновить задачу по ID',
        description='Обновить задачу по ID',
    ),
    destroy=extend_schema(
        summary='Удалить задачу по ID',
        description='Удалить задачу по ID',
    ),
    patch=extend_schema(
        summary='Обновить задачу по ID',
        description='Обновить задачу по ID',
    ),
    execute=extend_schema(
        summary='Пометить задачу как выполнено',
        description='Пометить задачу как выполнено',
    ),
)
class TaskViewSet(
    ByUserCreatedMixin,
    MethodMatchingViewSetMixin,
    ModelViewSet,
):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    action_serializers = {
        'list': TaskSerializer,
        'create': TaskCreateSerializer,
        'update': TaskUpdateSerializer,
        'patch': TaskUpdateSerializer,
        'execute': TaskExecuteSerializer,
    }

    @action(methods=['POST'], detail=True)
    def execute(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        instance = self.get_object()
        task = TaskService.mark_task_as_done(
            instance=instance,
            user=request.user
        )
        return Response(data=TaskSerializer(task).data, status=status.HTTP_200_OK)
