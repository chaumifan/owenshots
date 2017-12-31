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
            await channel.send(img_dict[cmd])
        if message.content == ("!8ballchau"):
            await channel.send(random.choice(phrase))

    await bot.process_commands(message)

@bot.command(description="Description of test")
async def echo(ctx, *args):
    """Testing function"""
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

@bot.command()
async def repeat(ctx, times : int, content="repeating..."):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def eightballchau(ctx):
    await ctx.send(random.choice(phrase))

@bot.command()
async def kek(ctx):
    await ctx.send(lol)

@bot.command()
async def wagecuckalarm(ctx):
    alarm_emoji = u'\u23F0'
    await ctx.send(alarm_emoji + "WEE WOO WEE WOO" + alarm_emoji)
    await ctx.send(alarm_emoji + "WAGE CUCKS GO TO SLEEP" + alarm_emoji)
    await ctx.send(alarm_emoji + "WEE WOO WEE WOO" + alarm_emoji)

@bot.command()
async def repost(ctx):
    policecar_emoji = u'\U0001F693'
    await ctx.send(policecar_emoji + 
            "repost alert repost alert weewooweewooweewoo" +
            policecar_emoji)
    await ctx.send(policecar_emoji +
            "put the memes down and step away from the computer" +
            policecar_emoji)

@bot.command()
async def addimg(ctx, cmd, img):
    with open("image.info", "a") as f:
        f.write(cmd + " " + img)
    img_dict[cmd] = img

### REMOVED COMMANDS ###

lol = u'\u314b\u314b\u314b'
phrase = ["do your homework", 
        "cs?", 
        "take a hit?",
        "ruin someone's player experience",
        "draw two cards"]
cmd_list = [""]
img_dict = create_dict()

with open("token", "r") as f:
    token = f.readline()
bot.run(token[:-1])
