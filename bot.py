import discord
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix= ".")


@Bot.event
async def on_ready():
    print("Я онлайн!")


@Bot.event
async def on_ready():
    game = discord.Game(r"FizrualBot.io | .help")    
    await Bot.change_presence(status=discord.Status.idle, activity=game)


@Bot.command()
async def defqon(ctx):
    author = ctx.message.author
    await ctx.send("DefqonSploit is banned to the server!")

@Bot.command()
async def vk(ctx):
    author = ctx.message.author
    await ctx.send(f"Наша группа вк: https://vk.com/fizrualrp. Спросил {author.mention}")

@Bot.command()
async def steam(ctx):
    author = ctx.message.author
    await ctx.send("Наша группа стим: Скоро")





Bot.run("NjE1NTY1NjY0MTc4MDEyMTc1.XWP4XA.bYcbGzh8AEtb3e9cjTKaiNJ3JPM")
