import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")

@bot.command()
async def test(ctx, arg):
    if arg == "help":
        await ctx.send("List of commands: ")
    if arg == "8ballchau":
        await ctx.send("do your homework")
    else:
        await ctx.send(arg)
