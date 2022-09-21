from abc import abstractmethod


class Action:

    name = 'default_action_name'

    def func(self):
        pass

    @abstractmethod
    def activate(self, game_instance, unit, coords):
        pass

    @abstractmethod
    def can_be_activated(self, game_instance, unit, coords):
        pass
