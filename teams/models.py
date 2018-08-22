from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import TimeStampedModel
from users.models import User


class Team(TimeStampedModel):
    name = models.CharField(max_length=60)
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='teams'
    )
    integrants = models.ManyToManyField(
        User,
        related_name='integrants',
        through='Role',
        through_fields=('team', 'user')
    )


class Role(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    active = models.BooleanField(_('active'), default=False)
