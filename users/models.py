from django.db import models
from django.utils.translation import ugettext_lazy as _

from authtools.models import AbstractEmailUser


class User(AbstractEmailUser):
    user = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.email
