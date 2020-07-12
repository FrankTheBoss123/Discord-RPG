import random

def combat(character1,character2):
    if random.choice([True,False]):
        attacker = character1.copy()
        defender = character2.copy()
    else:
        attacker = character2.copy()
        defender = character1.copy()
    while True:
        skills.trigger_skill(attacker,defender,"on-attack")
        skills.trigger_skill(defender,attacker,"on-defence")
        damage = get_damage(attacker,defender)
        defender["stats"][0]-=damage
        skills.trigger_skill(attacker,defender,"on-hit")

        if not characters.isAlive(attacker):
            break
        if not characters.isAlive(defender):
            return

def get_damage(attacker,defender):


def 
