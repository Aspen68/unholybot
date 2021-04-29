import discord
from discord.ext import commands


class sendToGulagCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "sendtogulag",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def sendToGulagCog(self, ctx:commands.Context, *args):
        sendRoles = []
        for role in ctx.message.author.roles:
            sendRoles.append(role.name)
        if "admin" in sendRoles or "communist-robots" in sendRoles:
            guild_roles = []
            for role in ctx.message.guild.roles:
                guild_roles.append(role.name)
            if "prisoner" not in guild_roles:
                await ctx.send("Could not find the prisoner role, creating it")
                await ctx.message.guild.create_role(name="prisoner", hoist=True, mentionable=True)
                guild_roles = []
                for role in ctx.message.guild.roles:
                    guild_roles.append(role.name)
                if "prisoner" not in guild_roles:
                    await ctx.send("Failed to create role")
                else:
                    await ctx.send("Successfully created role")
            else:
                memberToSendToGulag = ctx.message.guild.get_member_named(ctx.message.mentions[0].name + "#" + ctx.message.mentions[0].discriminator)
                for role in ctx.message.mentions[0].roles:
                    if role.name == 'communist-robots' or role.name == "admin":
                        break 
                    if role.name == '@everyone':
                        continue
                    print(role)
                    await memberToSendToGulag.remove_roles(role)
                for roles in ctx.message.guild.roles:
                    if roles.name == "prisoner":
                        await memberToSendToGulag.add_roles(roles)
                        continue
            await ctx.send(f"{memberToSendToGulag} has been sent to the gulag!")
            memberID = f"<@{ctx.message.mentions[0].id}>"
            await ctx.message.guild.get_channel(837057629670866994).send(f"Welcome {memberID} to the gulag! Please pledge your allegiance to the soviet union by typing '#iserverthesovietunion'")
        else:
            await ctx.send("You're not allowed to send people to the gulag!")
            

def setup(bot:commands.Bot):
    bot.add_cog(sendToGulagCog(bot))
