import random

import weapons
import classes
import items

#stats index
# 0   1   2   3   4   5   6   7
#[hp,str,mag,skl,spd,lck,def,res]

new_player = {
    "weapon":items.get_item("stone sword"),
    "level":1,
    "xp":0,
    "max-xp":100,
    "class":"villager",
    "passive-skills":{},
    "active-skills":{},
    "unused-skills":[],
    "stats":[10,4,2,3,3,4,3,2],
    "max_stats":classes.get_max_stats("villager"),
    "growth_rate":classes.get_growth_rate("villager"),
}

def create_new_player():
    return new_player

def level_up(character):
    for num in range(len(character["stats"])):
        if random.random() < character["growth_rate"][num]:
            character["stats"][num]+=1
    character["level"]+=1
    character["xp"]=0
    if character["level"] == 15:
        character = add_skill(character,skills.get_skill(classes.get_skill(character["class"])))
    return character

def add_skill(character,skill):
    if skills.isActive(skill):
        skill_tag = skill["trigger"]
        if skill_tag not in character["active-skills"]:
            character["active-skills"][skill_tag] = []
        if skill not in character["active-skills"][skill_tag]:
            character["active-skills"][skill_tag].append(skill)
        return character
    else:
        if skill["name"] in character["passive-skills"]:
            return character
        character["passive-skills"][skill["name"]] = skill
        return character
