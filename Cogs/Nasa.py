import discord
from discord.ext import commands
import requests


class nasa(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "nasa",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def commandName(self, ctx:commands.Context, *args):
        url = 	"https://api.nasa.gov/planetary/apod"
        api_key = "LFczXdoRX015iytBaXmcNso9F6avk3sySxJ3i2xh"
        params = {"count": 1, "api_key": api_key}
        request = requests.get(url, params)
        data = request.json()
        await ctx.send(data[0]["hdurl"])
        await ctx.send("\nTitle: " + data[0]["title"] + "\nDate: " + data[0]["date"])
def setup(bot:commands.Bot):
    bot.add_cog(nasa(bot))