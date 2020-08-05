import random
import copy

import characters
import weapons
import skills

class battle:
    def __init__(self,character1,character2):
        self.winner, self.loser = self.fight(character1,character2)

    def combat(self,attacker,defender):
        skills.trigger_skill(attacker,defender,"on-attack")
        skills.trigger_skill(defender,attacker,"on-defence")
        damage = get_damage(attacker,defender)
        if get_crit(attacker,defender):
            damage*=2
        print(f"damage: {damage}")
        if get_hit(attacker,defender):
            defender["stats"][0]-=damage
            skills.trigger_skill(attacker,defender,"on-hit")
            print("hit")
        print("attacker stats: "+str(attacker["stats"]))
        print("defender stats: "+str(defender["stats"]))
        return attacker["stats"][0],defender["stats"][0]

    def fight(self,character1,character2):
        attacker = character1
        defender = character2
        while True:
            attacker["stats"][0],defender["stats"][0] = self.combat(copy.deepcopy(attacker),copy.deepcopy(defender))
            if attacker["stats"][0] <= 0:
                return defender,attacker
            if defender["stats"][0] <= 0:
                return attacker,defender
            attacker,defender = defender,attacker

    def get_winner(self):
        return self.winner

    def get_loser(self):
        return self.loser

def get_damage(attacker,defender):
    attacker_weapon, armour = attacker["weapon"], 0
    if defender["armour"]:
        armour = defender["armour"]["armour"]
    if weapons.is_magic(attacker_weapon):
        return attacker_weapon["power"]+(attacker["stats"][2]-defender["stats"][7])*2-armour
    else:
        return attacker_weapon["power"]+(attacker["stats"][1]-defender["stats"][6])*2-int(armour*1.25)

#might return a value higher than 100
def get_hit(attacker,defender):
    attacker_armour_weight, defender_armour_weight = 0, 0
    if attacker["armour"]:
        attacker_armour_weight = attacker["armour"]["weight"]
    if defender["armour"]:
        defender_armour_weight = defender["armour"]["weight"]
    print((50+(attacker["stats"][4]+defender["stats"][4])*2+(attacker["stats"][3]-defender["stats"][3])+(defender["weapon"]["weight"]-attacker["weapon"]["weight"]+defender_armour_weight-attacker_armour_weight)*3)/100)
    return rng((50+(attacker["stats"][4]+defender["stats"][4])*2+(attacker["stats"][3]-defender["stats"][3])+(defender["weapon"]["weight"]-attacker["weapon"]["weight"]+defender_armour_weight-attacker_armour_weight)*3)/100)

#might return a value higher than 100
def get_crit(attacker,defender):
    chance = ((attacker["stats"][1]-defender["stats"][1])*5+attacker["weapon"]["crit"])/100
    print(f"crit chance: {chance}")
    return rng(((attacker["stats"][1]-defender["stats"][1])*5+attacker["weapon"]["crit"])/100)

def rng(chance):
    if random.random() < chance:
        return True
    return False
