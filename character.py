import weapon
import class

#stats index
# 0   1   2   3   4   5   6   7
#[hp,str,mag,skl,spd,lck,def,res]

new_player = {
    "weapon":weapon.get_weapon("stone sword"),
    "class":"villager",
    "skills":None,
    "stats":[10,4,2,3,3,4,3,2],
    "max_stats":class.get_max_stats("villager"),
    "growth_rate":class.get_growth_rate("villager"),
}

def create_new_player():
    return new_player
