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
    
@bot.command(pass_context=True)
async def battleonbank(ctx):
    embed = discord.Embed(title="Battleon Bank", color=0x00a0ea)
    embed.set_thumbnail(url = "https://thumb.ibb.co/euN8un/AQ3_D_Logo_T_shirt.png")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def classtrainers(ctx):
    embed = discord.Embed(title="Class Trainers", color=0x00a0ea)
    embed.set_thumbnail(url = "https://thumb.ibb.co/euN8un/AQ3_D_Logo_T_shirt.png")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def cyseroforge(ctx):
    embed = discord.Embed(title="Cysero's Forge", color=0x00a0ea)
    embed.set_thumbnail(url = "https://thumb.ibb.co/euN8un/AQ3_D_Logo_T_shirt.png")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def guardiantower(ctx):
    embed = discord.Embed(title="Guardian Tower", color=0x00a0ea)
    embed.set_thumbnail(url = "https://thumb.ibb.co/euN8un/AQ3_D_Logo_T_shirt.png")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def magicshoppe(ctx):
    embed = discord.Embed(title="Magic Shoppe", color=0x00a0ea)
    embed.set_thumbnail(url = "https://thumb.ibb.co/euN8un/AQ3_D_Logo_T_shirt.png")
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def yulgarsinn(ctx):
    embed = discord.Embed(title="Yulgars Inn", color=0x00a0ea)
    embed.set_thumbnail(url = "https://thumb.ibb.co/euN8un/AQ3_D_Logo_T_shirt.png")
    await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def alphaknightarmor(ctx):
    embed = discord.Embed(title="Alpha Knight Armor", color=0x00a0ea)
    await bot.say(embed=embed) 
    await bot.say("https://thumb.ibb.co/k4gdKx/MflPmCe.png".format(ctx))
    await bot.say("```Found on: Melodia's Shop, Sanctuary```")

@bot.command(pass_context=True)
async def basicarmor(ctx):
    embed = discord.Embed(title="Basic Armor", color=0x00a0ea)
    await bot.say(embed=embed) 
    await bot.say("https://thumb.ibb.co/dBhw6c/fhoUF5K.png".format(ctx))
    await bot.say("```Found on: N/A```")    
@bot.command(pass_context=True)
async def battleonmilitiaarmor(ctx):
    embed = discord.Embed(title="Battleon Militia Armor", color=0x00a0ea)
    await bot.say(embed=embed) 
    await bot.say("https://thumb.ibb.co/j8z16c/n4AAzEc.png".format(ctx))
    await bot.say("```Found on: Battleon Militia Craft Shop (Seasonal)```")
@bot.command(pass_context=True)
async def betaberserkerarmor(ctx):
    embed = discord.Embed(title="Beta Berserker Armor", color=0x00a0ea)
    await bot.say(embed=embed) 
    await bot.say("https://thumb.ibb.co/fMz7ex/gSNqzbD.png".format(ctx))
    await bot.say("```Found on: Beta Berserker Crafting - Cysero Forge```")

@bot.command(pass_context=True)
async def betaberserkerarmor(ctx):
    embed = discord.Embed(title="Beta Berserker Armor", color=0x00a0ea)
    await bot.say(embed=embed) 
    await bot.say("https://thumb.ibb.co/fMz7ex/gSNqzbD.png".format(ctx))
    await bot.say("```Found on: Beta Berserker Crafting - Cysero Forge```")    
    

    
    
    
    
token = os.environ.get("sira")
bot.run(f'{token}')
