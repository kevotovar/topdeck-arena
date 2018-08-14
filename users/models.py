from django.db import models
from django.utils.translation import ugettext_lazy as _

from authtools.models import AbstractEmailUser


class User(AbstractEmailUser):
    pass
