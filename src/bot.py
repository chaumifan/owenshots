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
    if message.content == ("!DIY"):
        await client.send_file(channel,"my_image.png")
#    if message.content in img_dict:
#        await bot.say("found entry")
    if message.content == ("!8ballchau"):
        await bot.say("8 ball summoned")
    if message.content == "!stupid":
        await bot.say("it worked")
    if message.content == ("!no"):
        await bot.say("nooooo")

    await bot.process_commands(message)

@bot.command(pass_context=True)
async def foo(ctx):
    #    await bot.say("foo!")
    await ctx.send("foo!")

@bot.command()
async def repeat(times : int, content="repeating..."):
    for i in range(times):
        await bot.say(content)

@bot.command()
async def eightballchau():
    await bot.say(random.choice(phrase))

@bot.command(description="Description of test")
async def echo(*args):
    """Testing function"""
    await bot.say('{} arguments: {}'.format(len(args), ', '.join(args)))

@bot.command()
async def kek():
    await bot.say(lel)

@bot.command()
async def wagecuckalarm():
    await bot.say("WEE WOO WEE WOO")

@bot.command()
async def profanities():
    await bot.say()

lel = u'\u314b\u314b\u314b'
phrase = ["do your homework", 
        "play cs", 
        "take a hit",
        "ruin someone's player experience"]
img_dict = create_dict

with open("token", "r") as f:
    token = f.readline()
bot.run(token[:-1])
