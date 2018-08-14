from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """
    Timestamp model
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
