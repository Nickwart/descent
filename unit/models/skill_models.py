from unit.models.proxy_inheritance_model import BaseInheritanceModel
from abc import abstractmethod
from django.db import models


class Skill(BaseInheritanceModel):
    name = models.CharField(max_length=40)

    @abstractmethod
    def activate(self, game_instance, unit, coords):
        pass

    @abstractmethod
    def can_be_activated(self, game_instance, unit, coords):
        pass


# hero personal skills
class DefaultSindrael(Skill):

    class Meta:
        proxy = True

    name = 'default_sindrael'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


class UltraSindrael(Skill):

    class Meta:
        proxy = True

    name = 'ultra_sindrael'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


class DefaultGrisban(Skill):

    class Meta:
        proxy = True

    skill_name = 'default_grisban'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


class UltraGrisban(Skill):

    class Meta:
        proxy = True

    skill_name = 'ultra_grisban'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


class DefaultLeoric(Skill):

    class Meta:
        proxy = True

    name = 'default_leoric'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


class UltraLeoric(Skill):

    class Meta:
        proxy = True

    name = 'ultra_leoric'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


class DefaultAshrian(Skill):

    class Meta:
        proxy = True

    name = 'default_ashrian'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


class UltraAshrian(Skill):

    class Meta:
        proxy = True

    name = 'ultra_ashrian'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


# Warrior class skills
class OathOfHonor(Skill):

    class Meta:
        proxy = True

    name = 'oath_of_honor'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


class Rage(Skill):

    class Meta:
        proxy = True

    name = 'rage'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


# Healer class skills
class PrayerOfHealing(Skill):

    class Meta:
        proxy = True

    name = 'prayer_of_healing'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


class Stoneskin(Skill):

    class Meta:
        proxy = True

    name = 'stoneskin'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


# Mage class skills
class RaiseDead(Skill):

    class Meta:
        proxy = True

    name = 'raise_dead'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


class RunicKnowledge(Skill):

    class Meta:
        proxy = True

    name = 'runic_knowledge'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


# Stalker class skills
class Greedy(Skill):

    class Meta:
        proxy = True

    name = 'greedy'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass


class Nimble(Skill):

    class Meta:
        proxy = True

    name = 'nimble'

    def activate(self, game_instance, unit, coords):
        pass

    def can_be_activated(self, game_instance, unit, coords):
        pass
