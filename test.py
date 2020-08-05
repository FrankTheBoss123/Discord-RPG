import battles
import characters
import skills
import items
import classes

from battles import battle

player1 = characters.create_new_player()

print(player1["stats"])

classes.switch_class(player1,"ballistician")

print(player1["stats"])
