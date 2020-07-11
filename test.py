import classes
import skills
import items
import characters
import weapons

weapon = items.get_item("leather shield")

print(weapon)

weapon = weapons.enchant_item(weapon,weapons.get_enchant(5))

print(weapon)

weapon = weapons.remove_enchant(weapon)

print(weapon)
