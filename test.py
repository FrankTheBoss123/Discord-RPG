import battles
import characters
import skills
import items
import classes

from battles import battle

player1 = characters.create_new_player()
player2 = characters.create_new_player()

print(player1["max-health"])
print(player1["stats"])

characters.add_skill(player1,skills.get_skill("tomebreaker"))
characters.add_skill(player1,skills.get_skill("drain"))

classes.switch_class(player1,"greatknight")

fight = battle(player1,player2)

print(player1["max-health"])
print(player1["stats"])
