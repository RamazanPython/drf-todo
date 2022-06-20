from django.urls import path, include
from rest_framework.routers import SimpleRouter

from tasks.api.v1.views import TaskViewSet

router = SimpleRouter()
router.register(r'', TaskViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
