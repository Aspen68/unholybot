import discord
from discord.ext import commands
import requests


class vadskajagäta(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "vadskajagäta",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def commandName(self, ctx:commands.Context, *args):
        url = 	"https://api.spoonacular.com/recipes/random"
        api_key = "4bc1639124484aa78e99be8802f1c9b4"
        params = {"apiKey": api_key}
        request = requests.get(url, params)
        data = request.json()
        await ctx.send(data["recipes"][0]["spoonacularSourceUrl"])
def setup(bot:commands.Bot):
    bot.add_cog(vadskajagäta(bot))