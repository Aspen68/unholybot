import discord
from discord.ext import commands
import json

# Get configuration.json
with open("configuration.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    print(token)
    prefix = data["prefix"]
    watching = data["watching"]



class Greetings(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self._last_member = None

# Intents
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(prefix, intents = intents)

# Load cogs
initial_extensions = [
    "Cogs.help",
    "Cogs.ping",
    "Cogs.shalom",
    "Cogs.communistmanifesto",
    "Cogs.nuke",
    "Cogs.sendToGulag",
    "Cogs.iservethesovietunion",
    "Cogs.watching",
    "Cogs.privjet",
    "Cogs.randomGulag",
    "Cogs.giveFreeOnJoin"
]

print(initial_extensions)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {extension}")


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{watching}"))
    print(discord.__version__)

bot.run(token)