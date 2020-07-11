import json

#rememver to uncap the first letter for the index

def read():
    with open("/Users/Frank Peng/github/Discord-RPG/game_data/class_data.json","r") as w:
        file = json.load(w)
        w.close()
    return file


classes_data = read()

def get_max_stats(classname):
    return classes_data[classname]["max_stats"].copy()

def get_growth_rate(classname):
    return classes_data[classname]["growth_rate"].copy()

def get_skill(character,classname):
    return classes_data[classname]["skill"].copy()

character_gif = {
    "Lord":"https://cdn.discordapp.com/attachments/697941728375734363/700970098147721246/ezgif.com-gif-maker_38.gif",
    "Grandmaster":"https://vignette.wikia.nocookie.net/fireemblem/images/2/27/FE13_Sorcerer.gif",
    "General":"https://vignette.wikia.nocookie.net/fireemblem/images/c/c4/FE13_Chrom_Great_Lord.gif",
    "Hero":"https://vignette.wikia.nocookie.net/fireemblem/images/b/b6/FE13_Priam_Hero_Map_Sprite.gif",
    "Thug":"https://vignette.wikia.nocookie.net/fireemblem/images/9/94/FE13_Barbarian_Map_Sprite.gif",
    "Cavalier":"https://vignette.wikia.nocookie.net/fireemblem/images/5/56/FE13_Stahl_Cavalier_Map_Sprite.gif",
    "Ballista":"https://vignette.wikia.nocookie.net/fireemblem/images/e/ed/FE14_Leo_Ballistician_Map_Sprite.gif",
    "Sage":"https://vignette.wikia.nocookie.net/fireemblem/images/e/ec/FE13_Emmeryn_Sage_Map_Sprite.gif",
    "Mage":"https://vignette.wikia.nocookie.net/fireemblem/images/2/20/FE13_Ricken_Mage_Map_Sprite.gif",
    "Assassin":"https://vignette.wikia.nocookie.net/fireemblem/images/b/b8/FE13_Assassin.gif",
    "Solider":"https://vignette.wikia.nocookie.net/fireemblem/images/a/ae/FE13_Soldier.gif",
    "Tactician":"https://vignette.wikia.nocookie.net/fireemblem/images/f/f0/FE13_Robin_%28M%29_Grandmaster_Map_Sprite.gif",
    "Barbarian":"https://vignette.wikia.nocookie.net/fireemblem/images/2/25/FE13_Basilio_Warrior_Map_Sprite.gif",
    "Greatknight":"https://vignette.wikia.nocookie.net/fireemblem/images/d/d6/FE14_Xander_Paladin_Map_Sprite.gif",
    "Bowknight":"https://vignette.wikia.nocookie.net/fireemblem/images/a/ae/FE14_Luna_Bow_Knight_Map_Sprite.gif",
    "Mercenary":"https://vignette.wikia.nocookie.net/fireemblem/images/7/7e/FE14_Luna_Mercenary_Map_Sprite.gif",
    "Sniper":"https://vignette.wikia.nocookie.net/fireemblem/images/2/25/FE14_Anna_Adventurer_Map_Sprite.gif",
    "Vanguard":"https://vignette.wikia.nocookie.net/fireemblem/images/6/6b/FE14_Ike_Vanguard_Map_Sprite.gif",
    "Archer":"https://vignette.wikia.nocookie.net/fireemblem/images/5/55/FE14_Setsuna_Bowman_Map_Sprite.gif",
    "Spearmen":"https://vignette.wikia.nocookie.net/fireemblem/images/c/cf/FE14_Takumi_Basara_Map_Sprite.gif",
    "Warrior":"https://vignette.wikia.nocookie.net/fireemblem/images/e/ef/FE14_Rinkah_Blacksmith_Map_Sprite.gif",
    "Rogue":"https://vignette.wikia.nocookie.net/fireemblem/images/a/a1/FE14_Hinata_Oni_Savage_Map_Sprite.gif",
    "Monk":"https://vignette.wikia.nocookie.net/fireemblem/images/1/10/FE14_Tsukuyomi_Onmyoji_Map_Sprite.gif",
    "Villager":"https://vignette.wikia.nocookie.net/fireemblem/images/7/74/FE13_Donnel_Villager_Map_Sprite.gif",
    "Priest":"https://vignette.wikia.nocookie.net/fireemblem/images/4/4c/FE13_Libra_War_Monk_Map_Sprite.gif"
}
