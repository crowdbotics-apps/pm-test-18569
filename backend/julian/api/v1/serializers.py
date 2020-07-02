from rest_framework import serializers
from julian.models import Eventsapp


class EventsappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventsapp
        fields = "__all__"
