from django.db import models

from core.models import TimeStampedModel
from teams.models import Team


class Tournament(TimeStampedModel):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slots = models.IntegerField()
    teams = models.ManyToManyField(
        Team,
        related_name='tournaments',
        through='TournamentEntry',
        through_fields=('tournament', 'team')
    )


class TournamentEntry(TimeStampedModel):
    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    accepted = models.BooleanField(default=False)
