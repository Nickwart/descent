from unit.models.skill_models import (
    DefaultSindrael,
    DefaultGrisban,
    DefaultAshrian,
    DefaultLeoric,
    UltraSindrael,
    UltraGrisban,
    UltraAshrian,
    UltraLeoric,
)


SINDRAEL = {
    "side": "Hero",
    "name": "Sindrael",
    "unit_class": '',
    "search_range": 1,
    "speed": 4,
    "health": 12,
    "durability": 4,
    "block": {"gray": 1, "black": 0, "brown": 0},
    "fist": 4,
    "book": 3,
    "shield": 2,
    "eye": 2,
    "skills": [DefaultSindrael, UltraSindrael],
    "items": [],
}

GRISBAN = {
    "side": "Hero",
    "name": "Grisban",
    "search_range": 1,
    "main_class": "warrior",
    "speed": 3,
    "health": 14,
    "durability": 4,
    "block": {"gray": 1, "black": 0, "brown": 0},
    "fist": 5,
    "book": 2,
    "shield": 3,
    "eye": 1,
    "skills": [DefaultGrisban, UltraGrisban],
    "items": [],
}

ASHRIAN = {
    "side": "Hero",
    "name": "Ashrian",
    "search_range": 1,
    "speed": 5,
    "health": 10,
    "durability": 4,
    "block": {"gray": 1, "black": 0, "brown": 0},
    "fist": 2,
    "book": 2,
    "shield": 3,
    "eye": 4,
    "skills": [DefaultAshrian, UltraAshrian],
    "items": [],
}

LEORIC = {
    "side": "Hero",
    "name": "Leoric",
    "search_range": 1,
    "speed": 4,
    "health": 8,
    "durability": 5,
    "block": {"gray": 1, "black": 0, "brown": 0},
    "fist": 1,
    "book": 5,
    "shield": 2,
    "eye": 3,
    "skills": [DefaultLeoric, UltraLeoric],
    "items": [],
}
