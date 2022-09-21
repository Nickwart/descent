# Generated by Django 4.0.4 on 2022-06-28 20:11

from django.db import migrations, models


def items(apps, schema):
    Item = apps.get_model('unit', 'Item')
    Item.objects.all().delete()

    item_dict = {
        "IronLongsword": "iron_longsword",
        "WoodenShield": "wooden_shield",
        "ChippedGreataxe": "chipped_greataxe",
        "IronMace": "iron_mace",
        "OakStaff": "oak_staff",
        "ReapersScythe": "reapers_scythe",
        "ArcaneBolt": "arcane_bolt",
        "ThrowingKnives": "throwing_knives",
        "LuckyCharm": "lucky_charm",
        "YewShortbow": "yew_shortbow",
        "RandomTreasure": "random_treasure",

    }
    for item_class_name, item_object_name in item_dict.items():
        model = apps.get_model('unit', item_class_name)
        model.objects.create(name=item_object_name)


def items_reversal(apps, schema):
    model = apps.get_model('unit', 'Item')
    model.objects.all().delete()


def skills(apps, schema):
    Skill = apps.get_model('unit', 'Skill')
    Skill.objects.all().delete()

    skill_dict = {
        "DefaultSindrael": "default_sindrael",
        "UltraSindrael": "ultra_sindrael",
        "DefaultGrisban": "default_grisban",
        "UltraGrisban": "ultra_grisban",
        "DefaultAshrian": "default_ashrian",
        "UltraAshrian": "ultra_ashrian",
        "DefaultLeoric": "default_leoric",
        "UltraLeoric": "ultra_leoric",
        "OathOfHonor": "oath_of_honor",
        "Rage": "rage",
        "PrayerOfHealing": "prayer_of_healing",
        "Stoneskin": "stoneskin",
        "RaiseDead": "raise_dead",
        "RunicKnowledge": "runic_knowledge",
        "Greedy": "greedy",
        "Nimble": "nimble",
    }

    for skill_class_name, skill_object_name in skill_dict.items():
        model = apps.get_model('unit', skill_class_name)
        model.objects.create(name=skill_object_name)


def skills_reversal(apps, schema):
    model = apps.get_model('unit', 'Skill')
    model.objects.all().delete()


def dices(apps, schema):
    model = apps.get_model('unit', 'Dice')
    model.objects.all().delete()

    dice_list = ['black', 'gray', 'brown', 'yellow', 'blue', 'red']

    for dice in dice_list:
        model.objects.create(dice_type=dice)


def dices_reversal(apps, schema):
    """Reversal is NOOP since display_name is simply dropped during reverse"""
    model = apps.get_model('unit', 'Dice')
    model.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(items, items_reversal),
        migrations.RunPython(skills, skills_reversal),
        migrations.RunPython(dices, dices_reversal),
    ]
