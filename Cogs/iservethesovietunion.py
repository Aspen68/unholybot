import discord
from discord.ext import commands


class iserverthesovietunionCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "iservethesovietunion",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def iserverthesovietunion(self, ctx:commands.Context):
        if ctx.message.channel.name == "gulag":
            memberToRelease = ctx.message.guild.get_member_named(ctx.message.author.name + "#" + ctx.message.author.discriminator)
            memberRoles = []
            for role in ctx.message.author.roles:
                memberRoles.append(role.name)
            if "prisoner" in memberRoles:
                for role in memberToRelease.roles:
                    if role.name == '@everyone':
                        continue
                    await memberToRelease.remove_roles(role)
            print(ctx.message.guild.roles)
            for roles in ctx.message.guild.roles:
                    if roles.name == "Free":
                        await memberToRelease.add_roles(roles)
                        continue
        else:
            await ctx.send("You're already free... for now")


def setup(bot:commands.Bot):
    bot.add_cog(iserverthesovietunionCog(bot))