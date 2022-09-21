from django.contrib.auth.models import User
from unit.models.action_models import Action
from unit.models.status_models import Status
from unit.models.skill_models import Skill
from unit.models.item_models import Item
from unit.models.dice_model import Dice
from django.apps import apps
from django.db import models


class UnitManager(models.Manager):
    def create(self, **kwargs):
        unit_many_to_many = {}
        for param in kwargs.copy().keys():
            if param in ['skills', 'items', 'block']:
                unit_many_to_many[param] = kwargs[param]
                kwargs.pop(param)

        unit = super(UnitManager, self).create(**kwargs)

        dice_dict = unit_many_to_many['block']
        for key in dice_dict.keys():
            for i in range(dice_dict[key]):
                unit.block.add(Dice.objects.get(dice_type=key))
                unit.save()

        skill_item = {'Skill': 'skills', 'Item': 'items'}
        for obj_class, obj in skill_item.items():
            model = apps.get_model('unit', obj_class)
            for many_to_many_obj in unit_many_to_many[obj]:
                unit.__getattribute__(obj).add(model.objects.get(name=many_to_many_obj.name))

        return unit


class Unit(models.Model):

    objects = UnitManager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    side = models.CharField(max_length=30)
    unit_class = models.CharField(max_length=30, default='default_unit_class')
    moves = models.IntegerField(default=2)
    search_range = models.IntegerField()
    speed = models.IntegerField()
    max_speed = models.IntegerField(default=0)
    current_speed = models.IntegerField(default=0)
    health = models.IntegerField()
    max_health = models.IntegerField(default=0)
    current_health = models.IntegerField(default=0)
    durability = models.IntegerField()
    max_durability = models.IntegerField(default=0)
    current_durability = models.IntegerField(default=0)
    fist = models.IntegerField()
    book = models.IntegerField()
    shield = models.IntegerField()
    eye = models.IntegerField()
    x_coord = models.IntegerField(default=None, null=True)
    y_coord = models.IntegerField(default=None, null=True)
    block = models.ManyToManyField(Dice, related_name='block')
    max_block = models.ManyToManyField(Dice, related_name='max_block')
    current_block = models.ManyToManyField(Dice, related_name='current_block')
    skills = models.ManyToManyField(Skill)
    items = models.ManyToManyField(Item)
    actions = models.ManyToManyField(Action)
    statuses = models.ManyToManyField(Status)
