import descent_engine_core
from descent_engine_core.actions import pick_up_treasure, move_unit, add_speed_for_stamina
from descent_engine_core.exeptions.exeption import WrongHeroClassException
from descent_engine_core.unit_core_and_templates.bubuka_template import DEFAULT_BUBUKA
from descent_engine_core.unit_core_and_templates.hero_templates import SINDRAEL, GRISBAN
from descent_engine_core.unit_core_and_templates.hero_class_templates import KNIGHT, BERSERKER


class Unit:
    name = "default_unit_class_name"

    side = 'default_side'

    moves = 2

    search_range = 0

    speed = 0
    max_speed = 0
    current_speed = 0

    health = 0
    max_health = 0
    current_health = 0

    durability = 0
    max_durability = 0
    current_durability = 0

    block = {"gray": 0, "black": 0, "brown": 0}
    max_block = {"gray": 0, "black": 0, "brown": 0}
    current_block = {"gray": 0, "black": 0, "brown": 0}

    fist = 0
    book = 0
    shield = 0
    eye = 0

    skills = []
    items = []
    actions = []
    statuses = []

    x_coord = 0
    y_coord = 0

    def mock(self):
        pass

    def restore_unit(self, hero_params):

        for param, value in hero_params.items():
            setattr(self, param, value)

        names = ["skills", "items", "actions", "statuses"]
        for name in names:
            counter = 0
            for attr_name in getattr(self, name):
                getattr(self, name)[counter] = getattr(getattr(descent_engine_core, name), attr_name)
                counter += 1

        return self

    def archive_unit(self):

        hero_attributes = [attribute for attribute in dir(self) if not attribute.startswith("__")]
        hero_stats = {
            stat_name: getattr(self, stat_name)
            for stat_name in hero_attributes
            if type(getattr(self, stat_name)) != type(self.mock)
        }

        for key, value in hero_stats.items():
            list_of_skills_or_items = []
            if key in ["skills", "items", "statuses", 'actions']:
                for stat in hero_stats[key]:
                    list_of_skills_or_items.append(stat.name)

                hero_stats[key] = list_of_skills_or_items

        return hero_stats


class Hero(Unit):
    def __init__(self, hero_template, hero_class):
        if hero_class in hero_template["classes"]:

            for attr, value in hero_template.items():
                if attr not in ['skills', 'items', 'classes']:
                    setattr(self, attr, value)

            self.side = 'Hero'
            self.skills = hero_template["skills"] + hero_class["skills"]
            self.items = hero_template["items"] + hero_class["items"]
            self.actions = [pick_up_treasure, move_unit, add_speed_for_stamina]

        else:
            raise WrongHeroClassException


class Bubuka(Unit):
    def __init__(self, bubuka_template):
        for attr, value in bubuka_template.items():
            setattr(self, attr, value)
        self.side = 'Bubuka'
        self.actions = [move_unit]


# special heroes to develop and debug
debug_hero = Hero(SINDRAEL, KNIGHT)
debug_hero2 = Hero(GRISBAN, BERSERKER)
debug_bubuka = Bubuka(DEFAULT_BUBUKA)

print(debug_hero)
