from unit.models.proxy_inheritance_model import BaseInheritanceModel
from django.db import models


class Item(BaseInheritanceModel):
    name = models.CharField(max_length=40)


class IronLongsword(Item):

    class Meta:
        proxy = True

    name = 'iron_longsword'


class WoodenShield(Item):

    class Meta:
        proxy = True

    name = 'wooden_shield'


class ChippedGreataxe(Item):

    class Meta:
        proxy = True

    name = 'chipped_greataxe'


class IronMace(Item):

    class Meta:
        proxy = True

    name = 'iron_mace'


class OakStaff(Item):

    class Meta:
        proxy = True

    name = 'oak_staff'


class ReapersScythe(Item):

    class Meta:
        proxy = True

    name = 'reapers_scythe'


class ArcaneBolt(Item):

    class Meta:
        proxy = True

    name = 'arcane_bolt'


class ThrowingKnives(Item):

    class Meta:
        proxy = True

    name = 'throwing_knives'


class LuckyCharm(Item):

    class Meta:
        proxy = True

    name = 'lucky_charm'


class YewShortbow(Item):

    class Meta:
        proxy = True

    name = 'yew_shortbow'


class RandomTreasure(Item):

    class Meta:
        proxy = True

    name = 'random_treasure'
