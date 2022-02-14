from django.db import models
from model_utils.models import TimeStampedModel

class Deck(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_reviewed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title