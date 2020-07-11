import discord
from discord.ext.commands import Bot
import json

import characters
import weapons
import classes
import items
import skills
import battles

#add a system in add_skill to limit the skills that a player can have equiped at one time to be 5
#add a system so that when the player switches classes that if the cross the max stats change it to be limited by the max stats
#test how the all the skill functions works with a active skill

TOKEN = ""
file_path = "C:\Users\Frank Peng\github\Discord-RPG\game_data\user_data.json"
BOT_PREFIX = ["."]

class RpgBot:
    def __init__(self, token):
        self.data = self.read()
        self.client = Bot(command_prefix=BOT_PREFIX)
        self.token = token

        self.prepare_client()

    def run(self):
        self.client.run(self.token)

    def prepare_client(self):
        @self.client.event
        async def on_ready():
            self.add_all_player()
            self.write(self.data)
            print("ready for an adventure")

        @self.client.command()
        async def daily(ctx):
            print("still under-dev")

        @self.client.command()
        async def weekly(ctx):
            print("still under-dev")

        @self.client.command()
        async def mine(ctx):
            print("still under-dev")

        @self.client.command()
        async def fish(ctx):
            print("still under-dev")

        @self.client.command()
        async def chop(ctx):
            print("still under-dev")

        @self.client.command()
        async def shop(ctx):
            print("still under-dev")

    def add_all_player(self):
        for user in self.client.get_all_members():
            if str(user.id) not in self.data:
                self.add_player(user)

    def add_player(self,user):
        self.data[user_id] = {}
        self.data[user_id]["money"] = 0
        self.data[user_id]["character"] = character.create_new_player()
        self.data[user_id]["inventory"] = [None,None,None,None,None]

    def read(self):
        with open(file_path,"r") as w:
            file = json.load(w)
            w.close()
        return file

    def write(self,newfile):
        with open(file_path,"w") as w:
            json.dump(newfile,w,indent=4)
        w.close()

if __name__ == '__main__':
    bot = RpgBot(TOKEN)
    bot.run()
