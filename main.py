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
#check the player stat that's it's not over max health

TOKEN = ""
file_path = "/home/pi/Atom/Github_WorkSpace/Discord-RPG/game_data/user_data.json"
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
        async def stat(ctx):
            user_id = str(ctx.message.author.id)
            StatEmbed = discord.Embed(colour=discord.Colour.red(),description=str(self.data[user_id]))
            await ctx.send(embed=StatEmbed)

        @self.client.command()
        async def daily(ctx):
            user_id = str(ctx.message.author.id)
            boolean, time_diff = self.check_daily(user_id)
            if boolean:
                await ctx.send("You got 20 bucks")
                self.add_money(user_id,20)
            else:
                await ctx.send(f"{str(datetime.timedelta(seconds=(86400-time_diff)))} cooldown")

        @self.client.command()
        async def weekly(ctx):
            user_id = str(ctx.message.author.id)
            boolean, time_diff = self.check_weekly(user_id)
            if boolean:
                await ctx.send("You got 100 bucks")
                self.add_money(user_id,100)
            else:
                await ctx.send(f"{str(datetime.timedelta(seconds=(604800-time_diff)))} cooldown")

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
                self.add_player(str(user.id))

    def add_player(self,user_id):
        self.data[user_id] = {}
        self.data[user_id]["money"] = 0
        self.data[user_id]["character"] = characters.create_new_player()
        self.data[user_id]["inventory"] = [None,None,None,None,None]

    def check_daily(self,user_id):
        if user_id not in daily:
            daily[user_id] = datetime.datetime.now()
            return True,None
        else:
            seconds_difference = int((datetime.datetime.now()-daily[user_id]).total_seconds())
            if seconds_difference>=86400:
                daily[user_id] = datetime.datetime.now()
                return True,None
            return False,seconds_difference

    def check_weekly(self,user_id):
        if user_id not in weekly:
            weekly[user_id] = datetime.datetime.now()
            return True,None
        else:
            seconds_difference = int((datetime.datetime.now()-weekly[user_id]).total_seconds())
            print(seconds_difference)
            if seconds_difference>=604800:
                weekly[user_id] = datetime.datetime.now()
                return True,None
            return False,seconds_difference

    def add_money(self,user_id,amount):
        self.data[user_id]["money"]+=amount
        self.write(self.data)

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
