import random
import copy

import weapons
import classes
import items
import skills

#stats index
# 0   1   2   3   4   5   6   7
#[hp,str,mag,skl,spd,lck,def,res]

new_player = {
    "weapon":items.get_item("stone sword"),
    "armour":items.get_item("leather shield"),
    "level":1,
    "xp":0,
    "max-xp":100,
    "class":None,
    "passive_skills":{},
    "active_skills":{},
    "skills":[],
    "stats":[10,4,2,3,3,4,3,2],
    "class_stats":[0,0,0,0,0,0,0,0],
    "growth_rate":classes.get_growth_rate("villager"),
}

def create_new_player():
    player = copy.deepcopy(new_player)
    classes.switch_class(player,"villager")
    return player

def is_alive(character):
    return character["stats"][0] > 0

def level_up(character):
    for num in range(len(character["stats"])):
        if random.random() < character["growth_rate"][num]:
            character["stats"][num]+=1
    character["level"]+=1
    character["xp"]-=character["max-xp"]
    character["max-xp"]*=1.1
    if character["level"] == 15:
        character = add_skill(character,skills.get_skill(classes.get_skill(character["class"])))
    return character

def add_xp(character,amount):
    if "misc" in character["active_skills"]:
        if "veteran" in character["active_skills"]["misc"]:
            character["xp"]+=int(amount*1.25)
    else:
        character["xp"]+=amount
    while character["xp"]>=character["max-xp"]:
        level_up(character)

def add_skill(character,skill):
    if skill["name"] in character["skills"]:
        return
    if skills.isActive(skill):
        skill_tag = skill["trigger"]
        if skill_tag not in character["active_skills"]:
            character["active_skills"][skill_tag] = []
        if skill not in character["active_skills"][skill_tag]:
            character["active_skills"][skill_tag].append(skill)
    else:
        if skill["name"] in character["passive_skills"]:
            return
        character["passive_skills"][skill["name"]] = skill
        skills.apply_passive_skill(character,skill["effected_stat"],skill["amount"])

def remove_skill(character,skill):
    if skills.isActive(skill):
        if skill in character["active_skills"][skill["trigger"]]:
            character["active_skills"][skill["trigger"]].remove(skill)
            character["skills"].append(skill["name"])
    else:
        if skill["name"] in character["passive_skills"]:
            del character["passive_skills"][skill["name"]]
            character["skills"].append(skill["name"])
            skills.remove_passive_skill(character,skill["effected_stat"],skill["amount"])

def add_item(player,item):
    print("under dev")
