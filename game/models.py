from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from lobby.models import Lobby
from django.db import models


class Map(models.Model):
    name = models.CharField(max_length=55)
    map = models.JSONField()


class Game(models.Model):
    round_number = models.IntegerField(default=0)
    name = models.CharField(max_length=55, unique=False, default=None)
    lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE)
    map = models.OneToOneField(Map, on_delete=models.CASCADE, null=True)


class MapTemplate(models.Model):
    class MapTemplateType(models.TextChoices):
        PUBLIC = 'PU', _('Public')
        PRIVATE = 'PR', _('Private')
        DEFAULT = 'DF', _('Default')
        DEVELOPER = 'DV', _('Developer')

    name = models.CharField(max_length=55, unique=False)
    map = models.JSONField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=2,
        choices=MapTemplateType.choices,
        default=MapTemplateType.PUBLIC,
    )
