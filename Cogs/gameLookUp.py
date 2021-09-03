import discord
from discord.ext import commands
import requests


class game(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "game",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def commandName(self, ctx:commands.Context, *args):
        url = 	"https://www.cheapshark.com/api/1.0/games?"
        game = ""
        for i in args:
            game = game + " " + i
        params = {"title": game, "limit":10}
        request = requests.get(url, params)
        data = request.json()
        for i in data:
            await ctx.send("Game: " + i["external"] + "\n" "cheapest price: " + i["cheapest"] + "\n" "cheapest deal ID: " + i["cheapestDealID"])

def setup(bot:commands.Bot):
    bot.add_cog(game(bot))