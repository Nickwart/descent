from unit.models.skill_models import (
    OathOfHonor,
    Rage,
    PrayerOfHealing,
    Stoneskin,
    RaiseDead,
    RunicKnowledge,
    Greedy,
    Nimble)
from unit.models.item_models import (
    IronLongsword,
    WoodenShield,
    ChippedGreataxe,
    IronMace,
    OakStaff,
    ReapersScythe,
    ArcaneBolt,
    ThrowingKnives,
    LuckyCharm,
    YewShortbow)


# Warrior archetype classes
KNIGHT = {
    "skills": [OathOfHonor],
    "items": [IronLongsword, WoodenShield],
    "unit_class": "knight",
}
BERSERKER = {"skills": [Rage], "items": [ChippedGreataxe], "unit_class": "berserker"}

# Healer archetype classes
DISCIPLE = {
    "skills": [PrayerOfHealing],
    "items": [IronMace, WoodenShield],
    "unit_class": "disciple",
}
SPIRITSPEAKER = {"skills": [Stoneskin], "items": [OakStaff], "unit_class": "spiritspeaker"}

# Mage archetype classes
NECROMANCER = {
    "skills": [RaiseDead],
    "items": [ReapersScythe],
    "unit_class": "necromancer",
}
RUNEMASTER = {
    "skills": [RunicKnowledge],
    "items": [ArcaneBolt],
    "unit_class": "runemaster",
}

# Scout archetype classes
THIEF = {"skills": [Greedy], "items": [ThrowingKnives, LuckyCharm], "unit_class": "thief"}
WILDLANDER = {"skills": [Nimble], "items": [YewShortbow], "unit_class": "wildlander"}
