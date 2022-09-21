import uuid
from django.db import models
from django.contrib.auth.models import User
from unit.models.unit_model import Unit


class Lobby(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=55)
    private = models.BooleanField(default=False)
    password = models.CharField(max_length=55)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    users = models.ManyToManyField(User, through="lobby.LobbyUser", related_name='users')


class LobbyUser(models.Model):
    lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hero = models.OneToOneField(Unit, default=None, blank=True, null=True, on_delete=models.CASCADE)
