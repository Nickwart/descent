import random


class Dice:
    def __init__(self, dice_sides):
        self.dice_sides = dice_sides

    def get_random_dice_side(self):
        random.choice(self.dice_sides)
        print(random.choice(self.dice_sides))


BLUE_DICE = Dice([
        "X",
        {"Hearts": 1, "Flashes": 1},
        {"Hearts": 2, "Flashes": 0},
        {"Hearts": 2, "Flashes": 1},
        {"Hearts": 1, "Flashes": 0},
        {"Hearts": 2, "Flashes": 0}
    ])

RED_DICE = Dice([
        {"Hearts": 2, "Flashes": 0},
        {"Hearts": 2, "Flashes": 0},
        {"Hearts": 2, "Flashes": 0},
        {"Hearts": 1, "Flashes": 0},
        {"Hearts": 3, "Flashes": 0},
        {"Hearts": 3, "Flashes": 1}
    ])

YELLOW_DICE = Dice([
        {"Hearts": 0, "Flashes": 1},
        {"Hearts": 1, "Flashes": 0},
        {"Hearts": 1, "Flashes": 0},
        {"Hearts": 1, "Flashes": 1},
        {"Hearts": 2, "Flashes": 0},
        {"Hearts": 2, "Flashes": 1}
    ])

BLACK_DICE = Dice([
        {"Shields": 0},
        {"Shields": 2},
        {"Shields": 2},
        {"Shields": 2},
        {"Shields": 3},
        {"Shields": 4},
    ])

GRAY_DICE = Dice([
        {"Shields": 0},
        {"Shields": 1},
        {"Shields": 1},
        {"Shields": 1},
        {"Shields": 2},
        {"Shields": 3},
    ])

SHEET_DICE = Dice([
        {"Shields": 0},
        {"Shields": 0},
        {"Shields": 0},
        {"Shields": 1},
        {"Shields": 1},
        {"Shields": 2},
    ])

SHEET_DICE.get_random_dice_side()