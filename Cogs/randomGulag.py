import discord
from discord.ext import commands
import random

class gulagCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        rand = random.randint(0,100)
        if message.author.id != self.bot.user.id:   
            if rand == 1:
                roles = []
                for role in message.author.roles:
                    roles.append(role)
                if "admin" not in roles or "communist-robots" not in roles:
                    for role in roles:
                        if role.name == "@everyone":
                            continue
                        if role.name == "admin":
                            break
                        if role.name == "communist-robots":
                            break
                        await message.author.remove_roles(role)
                    for roles in message.guild.roles:
                        if roles.name == "prisoner":
                            await message.author.add_roles(roles)
                            continue
            
                memberID = f"<@{message.author.id}>"
                await message.guild.get_channel(837057629670866994).send(f"Welcome {memberID} to the gulag! Please pledge your allegiance to the soviet union by typing ```#iservethesovietunion I, a citizen of the Union of Soviet Socialist Republics, joining the ranks of the Workers' and Peasants' Red Army, do hereby take the oath of allegiance and do solemnly vow to be an honest, brave, disciplined and vigilant fighter, to guard strictly all military and State secrets, to obey implicitly all Army regulations and orders of my commanders, commissars and superiors. I vow to study the duties of a soldier conscientiously, to safeguard Army and National property in every way possible and to be true to my People, my Soviet Motherland, and the Workers' and Peasants' Government to my last breath. I am always prepared at the order of the Workers' and Peasants' Government to come to the defence of my Motherland - the Union of Soviet Socialist Republics - and, as a fighter of the Workers' and Peasants' Red Army, I vow to defend her courageously, skilfully, creditably and honourably, without sparing my blood and my very life to achieve complete victory over the enemy. And if through evil intent I break this solemn oath, then let the stern punishment of the Soviet law, and the universal hatred and contempt of the working people, fall upon me.```")
                await message.channel.send(f"Your message has angered Stalin! GET SENT TO THE GULAG <@{message.author.id}>")

def setup(bot:commands.Bot):
    bot.add_cog(gulagCog(bot))