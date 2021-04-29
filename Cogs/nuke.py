import discord
from discord.ext import commands


class nukeCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "nuke",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def nuke(self, ctx:commands.Context, *args):
        roles = ctx.message.author.roles
        userRoles = []
        for role in roles:
            userRoles.append(role)
        if ctx.message.author.id == "354953987159621633":
            await ctx.send(f"Fuck off {ctx.message.author.name}")
        else:
            if ctx.guild.get_role(813854393177866240) in userRoles:
                if args[0]:
                    await ctx.message.channel.purge(limit=int(args[0]) + 1)
                    await ctx.send(f"Deleted {args[0]} messages")
                else:
                    await ctx.send("Need to know how much to nuke")
            else:
                await ctx.send("no")


def setup(bot:commands.Bot):
    bot.add_cog(nukeCog(bot))