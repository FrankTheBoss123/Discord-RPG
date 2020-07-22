import json

def read():
    with open("/Users/Frank Peng/github/Discord-RPG/game_data/skill_data.json","r") as w:
        file = json.load(w)
        w.close()
    return file

skill_data = read()

def isActive(skill):
    return skill["active"]

def get_skill(skillname):
    return skill_data[skillname].copy()

def apply_passive_skill(character,skill_target,skill_effect):
    character["stats"][skill_target]+=skill_effect

def remove_passive_skill(character,skill_target,skill_effect):
    character["stats"][skill_target]-=skill_effect

def trigger_skill(attacker,defender,trigger_str):
    #work on it later
    a = 0
