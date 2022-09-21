from abc import abstractmethod


class Skill:
    name = "default_skill_class_name"

    @abstractmethod
    def activate(self, game_instance, unit, coords):
        pass

    @abstractmethod
    def can_be_activated(self, game_instance, unit, coords):
        pass

