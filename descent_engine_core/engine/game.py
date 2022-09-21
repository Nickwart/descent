import json
from descent_engine_core.map.map_core import Mapp
from descent_engine_core.unit_core_and_templates.unit_core import Hero
from descent_engine_core.exeptions.exeption import ToManyHeroesException
from descent_engine_core.unit_core_and_templates.hero_class_templates import KNIGHT
from descent_engine_core.unit_core_and_templates.hero_templates import GRISBAN


class Game:
    def __init__(self, map_name):
        self.game_map = Mapp()
        self.game_map.import_map(map_name)

    list_of_heroes = []

    def add_hero(self, hero):
        self.list_of_heroes.append(hero)
        if len(self.list_of_heroes) > 4:
            raise ToManyHeroesException

    def pause_game_for_overlord(self):
        print("here would be a pause for overlord")

    def save_game(self, filename):
        saved_heroes_stats = []

        for hero in self.list_of_heroes:
            saved_heroes_stats.append(hero.archive_unit())

        big_dict = {"heroes": saved_heroes_stats, "map": self.game_map.map_matrix}

        json_dump = json.dumps(big_dict)

        with open(filename, "w") as file:
            file.write(json_dump)
            file.close()

    def load_game(self, filename):
        load_game = json.load(open(filename))
        self.game_map.map_matrix = load_game["map"]
        for i in range(len(load_game["heroes"])):
            new_hero = Hero(GRISBAN, KNIGHT)
            restore_hero = Hero.restore_unit(new_hero, load_game["heroes"][i])

            self.list_of_heroes.append(restore_hero)
