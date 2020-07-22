import random

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

def is_alive(character):
    return character["stats"][0] > 0

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
    if skill["name"] in character["unused-skills"]:
        return
    if skills.isActive(skill):
        skill_tag = skill["trigger"]
        if skill_tag not in character["active-skills"]:
            character["active-skills"][skill_tag] = []
        if skill not in character["active-skills"][skill_tag]:
            character["active-skills"][skill_tag].append(skill)
    else:
        if skill["name"] in character["passive-skills"]:
            return
        character["passive-skills"][skill["name"]] = skill
        skills.apply_passive_skill(character,skill["effected_stat"],skill["amount"])

def remove_skill(character,skill):
    if skills.isActive(skill):
        if skill in character["active-skills"][skill["trigger"]]:
            character["active-skills"][skill["trigger"]].remove(skill)
            character["unused-skills"].append(skill["name"])
    else:
        if skill["name"] in character["passive-skills"]:
            del character["passive-skills"][skill["name"]]
            character["unused-skills"].append(skill["name"])
            skills.remove_passive_skill(character,skill["effected_stat"],skill["amount"])

def add_item(player,item):
    print("under dev")
