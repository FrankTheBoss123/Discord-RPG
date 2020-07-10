import json

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

def get_weapon(weapon_name):
    return weapon_data[weapon_name]

def enchant_item(item,enchant):
    item["enchant"] = enchant
    if "power" in item:
        item["power"]+=int(item["power"]*enchant["buffs"])
    else:
        item["armour"]+=int(item["armour"]*enchant["buffs"])
    return item
