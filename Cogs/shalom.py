import discord
from discord.ext import commands


class shalomCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "shalom",
                    usage="don't use",
                    description = "no")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def commandName(self, ctx:commands.Context):
        await ctx.send("salam aleikum")


def setup(bot:commands.Bot):
    bot.add_cog(shalomCog(bot))