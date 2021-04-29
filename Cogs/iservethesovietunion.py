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
    async def iserverthesovietunion(self, ctx:commands.Context, *args):
        if ctx.message.channel.name == "gulag":
            pledge = ""
            for arg in args:
                pledge = pledge + arg + " "
            print(pledge)
            if pledge == "I, a citizen of the Union of Soviet Socialist Republics, joining the ranks of the Workers' and Peasants' Red Army, do hereby take the oath of allegiance and do solemnly vow to be an honest, brave, disciplined and vigilant fighter, to guard strictly all military and State secrets, to obey implicitly all Army regulations and orders of my commanders, commissars and superiors. I vow to study the duties of a soldier conscientiously, to safeguard Army and National property in every way possible and to be true to my People, my Soviet Motherland, and the Workers' and Peasants' Government to my last breath. I am always prepared at the order of the Workers' and Peasants' Government to come to the defence of my Motherland - the Union of Soviet Socialist Republics - and, as a fighter of the Workers' and Peasants' Red Army, I vow to defend her courageously, skilfully, creditably and honourably, without sparing my blood and my very life to achieve complete victory over the enemy. And if through evil intent I break this solemn oath, then let the stern punishment of the Soviet law, and the universal hatred and contempt of the working people, fall upon me. ":
                memberToRelease = ctx.message.guild.get_member_named(ctx.message.author.name + "#" + ctx.message.author.discriminator)
                memberRoles = []
                for role in ctx.message.author.roles:
                    memberRoles.append(role.name)
                if "prisoner" in memberRoles:
                    for role in memberToRelease.roles:
                        if role.name == '@everyone':
                            continue
                        if role.name == "admin":
                            continue
                        if role.name == "communist-robots":
                            continue
                        await memberToRelease.remove_roles(role)
                print(ctx.message.guild.roles)
                for roles in ctx.message.guild.roles:
                        if roles.name == "Free":
                            await memberToRelease.add_roles(roles)
                            continue
                await ctx.message.guild.get_channel(646071916314230797).send(f"{memberToRelease} was released!")
            else:
                await ctx.send("Your pledge was wrong... DO IT AGAIN")
        else:
            await ctx.send("You're already free... for now")
            


def setup(bot:commands.Bot):
    bot.add_cog(iserverthesovietunionCog(bot))