import discord
from discord.ext import commands


class freeOnJoin(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        for role in member.guild.roles:
            if role.name == "Free":
                member.add_roles(role)

def setup(bot:commands.Bot):
    bot.add_cog(freeOnJoin(bot))