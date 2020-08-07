

def isFull(inventory):
    return len(inventory) >= 9

def add_weapon(inventory,item):
    inventory.append(item)

def remove_weapon(inventory,item):
    inventory.remove(item)

def locate_weapon(inventory,itemname):
    for num in range(len(inventory)):
        weapon = inventory[num]
        if weapon["name"] == itemname:
            return weapon
    return None

def has_resource(inventory,resourcename,amount):
    if resourcename in inventory:
        if inventory[resourcename]["amount"]>=amount:
            return True
    return False

def add_resource(inventory,resourcename,amount):
    if resourcename not in inventory:
        inventory[resourcename] = {}
        inventory[resourcename]["amount"] = amount
    else:
        inventory[resourcename]["amount"] += amount

def remove_resource(inventory,resourcename,amount):
    inventory[resourcename]["amount"]-=amount
    if inventory[resourcename]["amount"] <= 0:
        del inventory[resourcename]
