from rest_framework import authentication
from julian.models import Eventsapp
from .serializers import EventsappSerializer
from rest_framework import viewsets


class EventsappViewSet(viewsets.ModelViewSet):
    serializer_class = EventsappSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Eventsapp.objects.all()
