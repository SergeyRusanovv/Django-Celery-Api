from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet


app_name = "my_api"

router = routers.SimpleRouter()
router.register("task", TaskViewSet, basename="my_api")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
