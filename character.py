import random

import weapon
import class

#stats index
# 0   1   2   3   4   5   6   7
#[hp,str,mag,skl,spd,lck,def,res]

new_player = {
    "weapon":weapon.get_weapon("stone sword"),
    "level":1,
    "xp":0,
    "max-xp":100,
    "class":"villager",
    "passive-skills":{},
    "active-skills":{},
    "stats":[10,4,2,3,3,4,3,2],
    "max_stats":class.get_max_stats("villager"),
    "growth_rate":class.get_growth_rate("villager"),
}

def create_new_player():
    return new_player

def level_up(character):
    for num in range(len(character["stats"])):
        if random.random() < character["growth_rate"]:
            character["stats"][num]+=1
    character["level"]+=1
    character["xp"]=0
    if character["level"] == 15:
        character = add_skill(character,class.get_skill(character["class"]))
    return character

def add_skill(character,skill):
    if skill.isActive(skill):
        character
