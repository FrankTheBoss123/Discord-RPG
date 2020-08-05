import battles
import characters
import skills
import items

from battles import battle

player1 = characters.create_new_player()
player2 = characters.create_new_player()

characters.add_skill(player1,skills.get_skill("drain"))
characters.add_skill(player2,skills.get_skill("counter-strike"))
player1["weapon"] = items.get_item("bolganone")

fight = battle(player1,player2)

print(fight.get_winner()["stats"])
