from django.db import models

from core.models import TimeStampedModel


class Customer(TimeStampedModel):
    pass


class Card(TimeStampedModel):
    pass


class Payment(TimeStampedModel):
    pass
