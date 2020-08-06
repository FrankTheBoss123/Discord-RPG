import json
import random

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

def trigger_skill(self,opponent,trigger_str):
    if trigger_str in self["active_skills"]:
        for skill in self["active_skills"][trigger_str]:
            if skill["target"] == "opponent":
                affected = opponent
            if skill["target"] == "self":
                affected = self
            if "trigger_rate" in skill:
                if isinstance(skill["trigger_rate"][0],str):
                    if opponent["weapon"]["type"] == skill["trigger_rate"][1]:
                        print(skill["name"])
                        affected["stats"][skill["affected_stat"]]+=skill["amount"]
                elif rng(self["stats"][skill["trigger_rate"][0]]/skill["trigger_rate"][1]/100):
                    print(skill["name"])
                    affected["stats"][skill["affected_stat"]]+=skill["amount"]
            else:
                print(skill["name"])
                affected["stats"][skill["affected_stat"]]+=skill["amount"]

def rng(chance):
    if random.random() < chance:
        return True
    return False
