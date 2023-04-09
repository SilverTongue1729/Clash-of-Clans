from characters import barbarians, dragons, balloons, archers, healers

lists = [barbarians, dragons, balloons, archers, healers]

def rage_spell(King):
    if King.alive == True:
        King.rage_effect()
    for list in lists:
        for unit in list:
            if unit.alive == True:
                unit.rage_effect()

def heal_spell(King):
    if King.alive == True:
        King.heal_effect()
    for list in lists:
        for unit in list:
            if unit.alive == True:
                unit.heal_effect()
