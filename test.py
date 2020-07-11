import classes
import skills
import items
import characters
import weapons

character = characters.create_new_player()

print(character["stats"])

characters.add_skill(character,skills.get_skill("sturdy"))

print(character["stats"])

characters.remove_skill(character,skills.get_skill("sturdy"))
characters.add_skill(character,skills.get_skill("sturdy"))
print(character["stats"])


print(character)
