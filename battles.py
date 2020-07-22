import random
import copy

import characters
import weapons
import skills

def combat(character1,character2):
    if random.choice([True,False]):
        attacker = copy.deepcopy(character1)
        defender = copy.deepcopy(character2)
    else:
        attacker = copy.deepcopy(character2)
        defender = copy.deepcopy(character1)
    a = 0
    while True:
        print(a)
        skills.trigger_skill(attacker,defender,"on-attack")
        skills.trigger_skill(defender,attacker,"on-defence")
        damage = get_damage(attacker,defender)
        if get_crit(attacker,defender):
            damage*=2
        print(f"damage: {damage}")
        if get_hit(attacker,defender):
            defender["stats"][0]-=damage
        skills.trigger_skill(attacker,defender,"on-hit")
        if not characters.is_alive(defender):
            print("defender loses")
            return
        if not characters.is_alive(attacker):
            print("attacker loses")
            return
        print("attacker stats: "+str(attacker["stats"]))
        print("defender stats: "+str(defender["stats"]))
        attacker,defender = defender,attacker
        a+=1
#stats index
# 0   1   2   3   4   5   6   7
#[hp,str,mag,skl,spd,lck,def,res]

def get_damage(attacker,defender):
    attacker_weapon = attacker["weapon"]
    if weapons.is_magic(attacker_weapon):
        return attacker_weapon["power"]+(attacker["stats"][2]-defender["stats"][7])*2+(attacker["stats"][3]-defender["stats"][3])-defender["armour"]["armour"]
    else:
        return attacker_weapon["power"]+(attacker["stats"][1]-defender["stats"][6])*2+(attacker["stats"][3]-defender["stats"][3])-int(defender["armour"]["armour"]*1.25)

#might return a value higher than 100
def get_hit(attacker,defender):
    chance = (60+(attacker["stats"][4]+defender["stats"][4])*2+(attacker["stats"][3]-defender["stats"][3])+(attacker["weapon"]["weight"]-defender["weapon"]["weight"])*3)/100
    print(f"hit chance: {chance}")
    return rng((50+(attacker["stats"][4]+defender["stats"][4])*2+(attacker["stats"][3]-defender["stats"][3])+(attacker["weapon"]["weight"]-defender["weapon"]["weight"])*3)/100)

#might return a value higher than 100
def get_crit(attacker,defender):
    chance = ((attacker["stats"][1]-defender["stats"][1])*5+attacker["weapon"]["crit"])/100
    print(f"crit chance: {chance}")
    return rng(((attacker["stats"][1]-defender["stats"][1])*5+attacker["weapon"]["crit"])/100)

def rng(chance):
    if chance <= 0:
        return False
    else:
        if random.random() < chance:
            return True
        return False
