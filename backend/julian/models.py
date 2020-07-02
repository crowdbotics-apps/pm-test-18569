from django.conf import settings
from django.db import models


class Eventsapp(models.Model):
    "Generated Model"
    date = models.DateField()
    location = models.CharField(max_length=256,)
    time = models.TimeField()
    horses = models.ForeignKey(
        "home.Location",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="eventsapp_horses",
    )


# Create your models here.
