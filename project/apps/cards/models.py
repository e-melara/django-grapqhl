from django.utils import timezone
from django.db import models
from model_utils.models import TimeStampedModel

from apps.decks.models import Deck

class Card(TimeStampedModel):
  deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
  question = models.TextField()
  answer = models.TextField()
  buckets = (
      (1, '1 Day'),
      (2, '3 Days'),
      (3, '7 Days'),
      (4, '16 Days'),
      (5, '30 Days'),
  )

  bucket = models.IntegerField(choices=buckets, default=1)
  next_review_at = models.DateTimeField(default=timezone.now())
  last_reviewed_at = models.DateTimeField(null=True, blank=True)

  def __str__(self):
    return self.question