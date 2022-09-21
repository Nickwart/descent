import os
import json
from descent_engine_core.map import map_templates as templates_module
from descent_engine_core.engine.game import Game
from unittest import TestCase
from descent_engine_core.unit_core_and_templates.unit_core import Hero
from descent_engine_core.unit_core_and_templates.hero_templates import GRISBAN
from descent_engine_core.unit_core_and_templates.hero_class_templates import KNIGHT


class GameStartTestCase(TestCase):
    path = os.path.abspath(templates_module.__file__)
    path_to_maps = path.replace("__init__.py", "map_for_tests.json")

    game_instance = Game(path_to_maps)
    hero = Hero(GRISBAN, KNIGHT)

    def test_hero_add(self):
        self.game_instance.add_hero(self.hero)
        self.assertEqual(self.game_instance.list_of_heroes[0], self.hero)

    def test_game_save(self):
        self.game_instance.add_hero(self.hero)
        self.game_instance.save_game("test_save.json")
        check_save = json.load(open("test_save.json"))

        self.assertEqual(check_save["heroes"][0]["name"], self.hero.name)
        self.assertEqual(check_save["heroes"][0]["moves"], self.hero.moves)
        self.assertEqual(check_save["heroes"][0]["search_range"], self.hero.search_range)
        self.assertEqual(check_save["heroes"][0]["speed"], self.hero.speed)
        self.assertEqual(check_save["heroes"][0]["health"], self.hero.health)
        self.assertEqual(check_save["heroes"][0]["durability"], self.hero.durability)
        self.assertEqual(check_save["heroes"][0]["block"], self.hero.block)
        self.assertEqual(check_save["heroes"][0]["fist"], self.hero.fist)
        self.assertEqual(check_save["heroes"][0]["book"], self.hero.book)
        self.assertEqual(check_save["heroes"][0]["shield"], self.hero.shield)
        self.assertEqual(check_save["heroes"][0]["eye"], self.hero.eye)
        self.assertEqual(check_save["heroes"][0]["x_coord"], self.hero.x_coord)
        self.assertEqual(check_save["heroes"][0]["y_coord"], self.hero.y_coord)

        os.remove("test_save.json")

    def test_game_load(self):
        self.game_instance.add_hero(self.hero)
        self.game_instance.save_game("test_save.json")
        self.game_instance.load_game("test_save.json")
        self.assertEqual(self.game_instance.list_of_heroes[0], self.hero)

        os.remove("test_save.json")
