import json
import items

def read():
    with open("/Users/Frank Peng/github/Discord-RPG/game_data/item_data.json","r") as w:
        file = json.load(w)
        w.close()
    return file

weapon_data = read()

enchants_data = [
    {"display_str":"I","buffs":0.2},
    {"display_str":"II","buffs":0.4},
    {"display_str":"III","buffs":0.6},
    {"display_str":"IV","buffs":0.8},
    {"display_str":"V","buffs":1.0}
]

def get_enchant(num):
    return enchants_data[num-1]

def rename_gear(gear,new_name):
    gear["display_name"] = new_name

def enchant_item(item,enchant):
    item["enchant"] = enchant
    if "power" in item:
        item["power"]+=int(item["power"]*enchant["buffs"])
    else:
        item["armour"]+=int(item["armour"]*enchant["buffs"])

def remove_enchant(item):
    if item["enchant"] != None:
        if "power" in item:
            print(items.get_item(item["name"]))
            item["power"] = items.get_item(item["name"])["power"]
        else:
            item["armour"] = items.get_item(item["name"])["armour"]
        item["enchant"] = None
