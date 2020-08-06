import battles
import characters
import skills
import items
import classes

from battles import battle

player1 = characters.create_new_player()
player2 = characters.create_new_player()

print(player1["stats"])

player2["weapon"] = items.get_item("bolganone")

characters.add_skill(player1,skills.get_skill("tomebreaker"))
characters.add_skill(player1,skills.get_skill("lethal"))

classes.switch_class(player1,"ballistician")

print(player1["stats"])

fight = battle(player1,player2)

print(fight.get_winner()["stats"])
