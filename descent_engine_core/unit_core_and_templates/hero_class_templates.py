from descent_engine_core.skills import (
    oath_of_honor,
    rage,
    prayer_of_healing,
    stoneskin,
    raise_dead,
    runic_knowledge,
    greedy,
    nimble,
)
from descent_engine_core.items import (
    iron_longsword,
    wooden_shield,
    chipped_greataxe,
    iron_mace,
    oak_staff,
    reapers_scythe,
    arcane_bolt,
    throwing_knives,
    lucky_charm,
    yew_shortbow,
)


# Warrior archetype classes
KNIGHT = {
    "skills": [oath_of_honor],
    "items": [iron_longsword, wooden_shield],
    "class": "knight",
}
BERSERKER = {"skills": [rage], "items": [chipped_greataxe], "class": "berserker"}

# Healer archetype classes
DISCIPLE = {
    "skills": [prayer_of_healing],
    "items": [iron_mace, wooden_shield],
    "class": "disciple",
}
SPIRITSPEAKER = {"skills": [stoneskin], "items": [oak_staff], "class": "spiritspeaker"}

# Mage archetype classes
NECROMANCER = {
    "skills": [raise_dead],
    "items": [reapers_scythe],
    "class": "necromancer",
}
RUNEMASTER = {
    "skills": [runic_knowledge],
    "items": [arcane_bolt],
    "class": "runemaster",
}

# Scout archetype classes
THIEF = {"skills": [greedy], "items": [throwing_knives, lucky_charm], "class": "thief"}
WILDLANDER = {"skills": [nimble], "items": [yew_shortbow], "class": "wildlander"}
