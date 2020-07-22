import discord
from discord.ext.commands import Bot
import json
import datetime

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

daily = {}
weekly = {}

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
            user_id = ctx.message.author.id
            if self.check_daily(user_id):
                await self.client.send("You got 20 bucks")
                self.add_money(user_id,20)
            else:
                await self.client.send(f"{str(datetime.timedelta(seconds=(86400-(datetime.datetime.now()-daily[user_id]))))} cooldown")

        @self.client.command()
        async def weekly(ctx):
            user_id = ctx.message.author.id
             if check_weekly(user_id):
                 await self.client.send("You got 100 bucks")
                 self.add_money(user_id,100)
             else:
                 await self.client.send(f"{str(datetime.timedelta(seconds=(604800-(datetime.datetime.now()-weekly[user_id]))))} cooldown")

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

    def check_daily(self,user_id):
        if user_id not in daily:
            daily[user_id] = datetime.datetime.now()
            return True
        else:
            if datetime.datetime.now()-daily[user_id]>=86400:
                daily[user_id] = datetime.datetime.now()
                return True
            return False

    def check_weekly(self,user_id):
        if user_id not in weekly:
            weekly[user_id] = datetime.datetime.now()
            return True
        else:
            if datetime.datetime.now()-weekly[user_id]>=604800:
                weekly[user_id] = datetime.datetime.now()
                return True
            return False

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
