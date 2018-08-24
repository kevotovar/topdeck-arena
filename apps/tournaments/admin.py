from django.contrib import admin
from . import models

admin.register(models.Tournament)
admin.register(models.TournamentEntry)
