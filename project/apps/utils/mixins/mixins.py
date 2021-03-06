from typing import Dict, Any


class MethodMatchingViewSetMixin:
    action_serializers = None

    def get_serializer_class(self):
        base_serializer = super(MethodMatchingViewSetMixin, self).get_serializer_class()
        return self.get_action_serializer_class().get(self.action, base_serializer)

    def get_action_serializer_class(self) -> Dict[str, Any]:
        return self.action_serializers or {}


class ByUserCreatedMixin:

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.action == 'list':
            return queryset

        user = self.request.user
        if user.is_superuser:
            return queryset

        return queryset.filter(created_by=user)
