from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import EventsappViewSet

router = DefaultRouter()
router.register("eventsapp", EventsappViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
