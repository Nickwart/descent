from descent_engine_core.unit_core_and_templates.hero_class_templates import (
    KNIGHT,
    BERSERKER,
    DISCIPLE,
    SPIRITSPEAKER,
    NECROMANCER,
    RUNEMASTER,
)
from descent_engine_core.skills import (
    default_sindrael,
    default_grisban,
    default_ashrian,
    default_leoric,
    ultra_sindrael,
    ultra_grisban,
    ultra_leoric,
    ultra_ashrian,
)


SINDRAEL = {
    "name": "Sindrael",
    "search_range": 1,
    "classes": [KNIGHT, BERSERKER],
    "speed": 4,
    "health": 12,
    "durability": 4,
    "block": {"gray": 1, "black": 0, "brown": 0},
    "fist": 4,
    "book": 3,
    "shield": 2,
    "eye": 2,
    "skills": [default_sindrael, ultra_sindrael],
    "items": [],
}

GRISBAN = {
    "name": "Grisban",
    "search_range": 1,
    "classes": [KNIGHT, BERSERKER],
    "main_class": "warrior",
    "speed": 3,
    "health": 14,
    "durability": 4,
    "block": {"gray": 1, "black": 0, "brown": 0},
    "fist": 5,
    "book": 2,
    "shield": 3,
    "eye": 1,
    "skills": [default_grisban, ultra_grisban],
    "items": [],
}

ASHRIAN = {
    "name": "Ashrian",
    "search_range": 1,
    "classes": [DISCIPLE, SPIRITSPEAKER],
    "speed": 5,
    "health": 10,
    "durability": 4,
    "block": {"gray": 1, "black": 0, "brown": 0},
    "fist": 2,
    "book": 2,
    "shield": 3,
    "eye": 4,
    "skills": [default_ashrian, ultra_ashrian],
    "items": [],
}

LEORIC = {
    "name": "Leoric",
    "search_range": 1,
    "classes": [NECROMANCER, RUNEMASTER],
    "speed": 4,
    "health": 8,
    "durability": 5,
    "block": {"gray": 1, "black": 0, "brown": 0},
    "fist": 1,
    "book": 5,
    "shield": 2,
    "eye": 3,
    "skills": [default_leoric, ultra_leoric],
    "items": [],
}
