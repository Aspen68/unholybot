import discord
from discord.ext import commands
import json


class watchingCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "watching",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def commandName(self, ctx:commands.Context, *args):
        if ctx.message.author.id == 210704118203809792:
            watching = ""
            for arg in args:
                watching = watching + arg + " "
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{watching}"))
            await ctx.send(f"now watching {watching}")
            with open("configuration.json", "r") as config:
                data = json.load(config)
                token = data["token"]
                prefix = data["prefix"]
            data = {
                    "token":token,
                    "prefix":prefix,
                    "watching":watching
            }
            with open("configuration.json", "w") as config:
                json.dump(data,config)

            
def setup(bot:commands.Bot):
    bot.add_cog(watchingCog(bot))