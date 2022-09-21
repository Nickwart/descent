import pytest
from unittest import TestCase
from descent_engine_core.unit_core_and_templates.unit_core import Hero
from descent_engine_core.unit_core_and_templates.hero_templates import ASHRIAN, SINDRAEL
from descent_engine_core.unit_core_and_templates.hero_class_templates import KNIGHT, NECROMANCER
from descent_engine_core.exeptions.exeption import WrongHeroClassException


class HeroTestCase(TestCase):
    def test_normal_hero_creation(self):
        hero = Hero(SINDRAEL, KNIGHT)
        self.assertEqual(hero.name, "Sindrael")

    @staticmethod
    def test_hero_creation_fails():
        with pytest.raises(WrongHeroClassException):
            Hero(ASHRIAN, NECROMANCER)
