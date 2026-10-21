from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.views import HealthCheckView, TaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health-check'),
] + router.urls
