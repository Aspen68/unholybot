import discord
from discord.ext import commands
import requests


class advice(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "advice",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def commandName(self, ctx:commands.Context):
        url = 	"https://api.adviceslip.com/advice"
        request = requests.get(url)
        data = request.json()
        await ctx.send(data["slip"]["advice"])

def setup(bot:commands.Bot):
    bot.add_cog(advice(bot))