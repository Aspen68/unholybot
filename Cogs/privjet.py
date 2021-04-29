import discord
from discord.ext import commands


class privjetCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "privjet",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def commandName(self, ctx:commands.Context):
        mention = f"<@{ctx.message.author.id}>"
        await ctx.send(f"Privjet comrade {mention}")


def setup(bot:commands.Bot):
    bot.add_cog(privjetCog(bot))