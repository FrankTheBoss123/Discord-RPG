import json

def read():
    with open("/Users/Frank Peng/github/Discord-RPG/game_data/item_data.json","r") as w:
        file = json.load(w)
        w.close()
    return file

item_data = read()

def get_item(item_name):
    if item_name in item_data:
        return item_data["item_data"]
    return None
