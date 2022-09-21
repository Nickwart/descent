from unit.models.proxy_inheritance_model import BaseInheritanceModel
from abc import abstractmethod


class Status(BaseInheritanceModel):

    @abstractmethod
    def activate(self, game_instance, unit, coords):
        pass

    @abstractmethod
    def can_be_activated(self, game_instance, unit, coords):
        pass


class Stunned(Status):

    class Meta:
        proxy = True

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


class Poisoned(Status):

    class Meta:
        proxy = True

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


class Fallen(Status):

    class Meta:
        proxy = True

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass
