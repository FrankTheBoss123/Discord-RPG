import json

#rememver to uncap the first letter for the index
#make a new skill for ballistician

def read():
    with open("/Users/Frank Peng/github/Discord-RPG/game_data/class_data.json","r") as w:
        file = json.load(w)
        w.close()
    return file

classes_data = read()

def get_class_stats(classname):
    return classes_data[classname]["class_stats"].copy()

def get_growth_rate(classname):
    return classes_data[classname]["growth_rate"].copy()

def get_skill(character,classname):
    return classes_data[classname]["skill"].copy()

def switch_class(character,newclassname):
    character["class"] = newclassname
    newclass_stats = get_class_stats(newclassname)
    for x in range(len(character["stats"])):
        if x == 0:
            character["max-health"]-=character["class_stats"][x]
            character["max-health"]+=newclass_stats[x]
        character["stats"][x]-=character["class_stats"][x]
        character["stats"][x]+=newclass_stats[x]
    character["class_stats"] = newclass_stats
