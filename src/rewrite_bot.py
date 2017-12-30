import random
from discord.ext import commands


bot = commands.Bot(command_prefix="!")

def create_dict():
    img_dict = {}
    with open("image.info", "r") as f:
        for line in f:
            (key, val) = line.split()
            img_dict[key] = val
    return img_dict

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")

@bot.event
async def on_message(message):
    channel = message.channel
    if message.content[0] == "!":
        cmd = message.content[1:]
        if cmd in img_dict:
            await channel.send("found entry")
            await channel.send(img_dict[cmd])
        if message.content == ("!8ballchau"):
            await channel.send("8 ball summoned")

    await bot.process_commands(message)

@bot.command()
async def foo(ctx):
    await ctx.send("foo!")

@bot.command()
async def repeat(ctx, times : int, content="repeating..."):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def eightballchau(ctx):
    await ctx.send(random.choice(phrase))

@bot.command(description="Description of test")
async def echo(ctx, *args):
    """Testing function"""
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

@bot.command()
async def kek(ctx):
    await ctx.send(lel)

@bot.command()
async def wagecuckalarm(ctx):
    await ctx.send("WEE WOO WEE WOO")

@bot.command()
async def addimg(ctx, cmd, img):
    with open("image.info", "a") as f:
        f.write(cmd + " " + img)
    img_dict[cmd] = img

### REMOVED COMMANDS ###

lel = u'\u314b\u314b\u314b'
phrase = ["do your homework", 
        "cs?", 
        "take a hit?",
        "ruin someone's player experience"]
img_dict = create_dict()

with open("token", "r") as f:
    token = f.readline()
bot.run(token[:-1])
