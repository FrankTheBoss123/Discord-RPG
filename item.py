import json

item_data = read()

def get_item(item_name):
    if item_name in item_data:
        return item_data["item_data"]
    return None

def read():
    with open("/home/pi/Atom/Discord_RPG/item_data.json","r") as w:
        file = json.load(w)
        w.close()
    return file
