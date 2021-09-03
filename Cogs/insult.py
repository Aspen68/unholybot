import discord
from discord.ext import commands
import requests


class insult(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "insult",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def commandName(self, ctx:commands.Context):
        url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
        request = requests.get(url)
        data = request.json()
        await ctx.send(data["insult"])

def setup(bot:commands.Bot):
    bot.add_cog(insult(bot))