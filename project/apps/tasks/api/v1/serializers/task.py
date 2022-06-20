from rest_framework import serializers

from tasks.models import Task
from utils.serializers import CreatedBySerializer
from users.api.v1.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'deadline',
            'is_done',
            'created_by',
            'created_date',
            'updated_date',
        )


class TaskCreateSerializer(
    CreatedBySerializer,
    serializers.ModelSerializer
):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'deadline',
            'created_by',
        )
        extra_kwargs = {
            'id': {'read_only': True},
        }


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'deadline',
            'is_done',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'title': {'required': False},
            'description': {'required': False},
            'deadline': {'required': False},
            'is_done': {'required': False},
        }


class TaskExecuteSerializer(serializers.Serializer):
    pass
