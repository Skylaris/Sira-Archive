import discord
from discord.ext import commands
import os
from discord.ext.commands import Bot
prefix = ["wiki."]
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Use wiki. for commands "))
    print("Bot online")



#https://discordapp.com/oauth2/authorize?client_id=430003755405279242&scope=bot
    
@bot.command(pass_context=True)
async def battleon(ctx):
    
    embed = discord.Embed(title="Battleon", color=0x00a0ea)
    embed.set_thumbnail(url = "https://thumb.ibb.co/euN8un/AQ3_D_Logo_T_shirt.png")
await bot.say(embed=embed)


token = os.environ.get("sira")
bot.run(f'{token}')
