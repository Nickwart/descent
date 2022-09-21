import os
from descent_engine_core.engine.game import Game
from unittest import TestCase
from unittest.mock import Mock
from descent_engine_core.map import map_templates as templates_module
from descent_engine_core.statuses import STUNNED, FALLEN
from descent_engine_core.unit_core_and_templates.unit_core import Hero, Bubuka
from descent_engine_core.unit_core_and_templates.hero_class_templates import KNIGHT
from descent_engine_core.unit_core_and_templates.bubuka_template import DEFAULT_BUBUKA
from descent_engine_core.unit_core_and_templates.hero_templates import GRISBAN, SINDRAEL
from descent_engine_core.actions import move_unit, pick_up_treasure


class HeroMovingTestCase(TestCase):
    path = os.path.abspath(templates_module.__file__)
    path_to_maps = path.replace("__init__.py", "first_blood_map_not_completed.json")

    game_instance = Game(path_to_maps)

    hero = Hero(SINDRAEL, KNIGHT)
    hero.y_coord = 3
    hero.x_coord = 4
    hero.current_speed = 6

    known_coords = {(3, 3): {'coords': [3, 3], 'cost_of_step': 1, 'previous_cell': [3, 4], 'cost_of_move': 1},
                    (4, 3): {'coords': [4, 3], 'cost_of_step': 1, 'previous_cell': [3, 4], 'cost_of_move': 1},
                    (4, 4): {'coords': [4, 4], 'cost_of_step': 1, 'previous_cell': [3, 4], 'cost_of_move': 1},
                    (5, 3): {'coords': [5, 3], 'cost_of_step': 2, 'previous_cell': [4, 3], 'cost_of_move': 1},
                    (5, 4): {'coords': [5, 4], 'cost_of_step': 2, 'previous_cell': [4, 3], 'cost_of_move': 1},
                    (6, 3): {'coords': [6, 3], 'cost_of_step': 4, 'previous_cell': [5, 4], 'cost_of_move': 2},
                    (6, 4): {'coords': [6, 4], 'cost_of_step': 4, 'previous_cell': [5, 4], 'cost_of_move': 2},
                    (6, 2): {'coords': [6, 2], 'cost_of_step': 3, 'previous_cell': [5, 3], 'cost_of_move': 1},
                    (7, 2): {'coords': [7, 2], 'cost_of_step': 4, 'previous_cell': [6, 2], 'cost_of_move': 1},
                    (7, 3): {'coords': [7, 3], 'cost_of_step': 5, 'previous_cell': [6, 2], 'cost_of_move': 2},
                    (8, 2): {'coords': [8, 2], 'cost_of_step': 5, 'previous_cell': [7, 2], 'cost_of_move': 1},
                    (8, 3): {'coords': [8, 3], 'cost_of_step': 6, 'previous_cell': [7, 2], 'cost_of_move': 2},
                    (7, 4): {'coords': [7, 4], 'cost_of_step': 6, 'previous_cell': [6, 3], 'cost_of_move': 2},
                    (7, 5): {'coords': [7, 5], 'cost_of_step': 6, 'previous_cell': [6, 4], 'cost_of_move': 2},
                    (9, 2): {'coords': [9, 2], 'cost_of_step': 6, 'previous_cell': [8, 2], 'cost_of_move': 1},
                    (9, 3): {'coords': [9, 3], 'cost_of_step': 6, 'previous_cell': [8, 2], 'cost_of_move': 1}}

    def test_get_move_list(self):
        move_list, step_list = move_unit.get_move_list(self.hero, self.hero.current_speed, self.game_instance)
        self.assertEqual(move_list, self.known_coords)

    def test_unit_movement(self):
        Game.pause_game_for_overlord = Mock()
        move_unit.activate(self.game_instance, self.hero, [7, 2])
        self.assertEqual([self.hero.y_coord, self.hero.x_coord], [7, 2])
        self.assertEqual(len(Game.pause_game_for_overlord.call_args_list), 3)


class TreasurePickUpTestCase(TestCase):
    path = os.path.abspath(templates_module.__file__)
    path_to_maps = path.replace("__init__.py", "first_blood_map_with_treasures.json")

    game_instance = Game(path_to_maps)

    hero = Hero(GRISBAN, KNIGHT)
    hero.y_coord = 3
    hero.x_coord = 8

    def test_treasure_picked_up(self):
        len_of_hero_items = len(self.hero.items)
        pick_up_treasure.activate(self.game_instance, self.hero, [3, 9])
        self.assertEqual(len(self.hero.items), len_of_hero_items + 1)
        self.assertEqual(self.game_instance.game_map.map_matrix[3][9], "F")

    def test_range_of_search(self):
        len_of_hero_items = len(self.hero.items)
        self.hero.search_range = 2
        pick_up_treasure.activate(self.game_instance, self.hero, [5, 10])
        self.assertEqual(len_of_hero_items+1, len(self.hero.items))
        self.assertEqual(self.game_instance.game_map.map_matrix[5][10], "F")

    def test_can_be_activated(self):
        pick_up_treasure.can_be_activated(self.game_instance, self.hero, [3, 9])
        y_coord_diff = abs(self.hero.y_coord - 3)
        x_coord_diff = abs(self.hero.x_coord - 9)
        self.assertEqual(self.hero.side,'Hero')
        self.assertEqual([STUNNED, FALLEN] not in self.hero.statuses, True)
        self.assertEqual(self.hero.moves > 0, True)
        self.assertEqual(y_coord_diff <= self.hero.search_range, True)
        self.assertEqual(x_coord_diff <= self.hero.search_range,True)

    def test_unit_side_is_right(self):
        request = pick_up_treasure.can_be_activated(self.game_instance, Bubuka(DEFAULT_BUBUKA), [0, 0])
        self.assertEqual(request, False)
