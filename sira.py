import discord
from discord.ext import commands
import os
from discord.ext.commands import Bot
prefix = [">>", ">", "->"]
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Use >>help for help. "))
    print("Bot online")


@bot.command()
async def hi():
    await bot.say("Idk")
    print("Done")
 
#invite
#https://discordapp.com/oauth2/authorize?client_id=430003755405279242&scope=bot

token = os.environ.get("sira")
bot.run(f'{token}')
