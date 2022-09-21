from django.db import models
import random


class Dice(models.Model):

    dice_type = models.CharField(max_length=20)

    sides = models.JSONField(null=True)

    def roll(self):
        random_choice = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
        pass
