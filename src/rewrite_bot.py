import random
import json
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

#async def alarm(self):
#    await self.wait_until_read()
#    channel = client.get_channel()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    channel = message.channel
    if message.content[0] == "!":
        cmd = message.content[1:]
        if cmd in img_dict:
            await channel.send(img_dict[cmd])
        if message.content == ("!8ballchau"):
            await channel.send(random.choice(phrase))

    if len(message.mentions) > 0 and message.author.id != owen_id:
        for member in message.mentions:
            if owen_id == member.id or owenbot_id == member.id:
                if message.author.id == cur_fav:
                    await channel.send(heart_emoji)
                else:
                    await channel.send("fuck you")

    if message.content == ("bet"):
        await channel.send("bet")

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
    await ctx.send(alarm_emoji + "WEE WOO WEE WOO" + alarm_emoji)
    await ctx.send(alarm_emoji + "WAGE CUCKS GO TO SLEEP" + alarm_emoji)
    await ctx.send(alarm_emoji + "WEE WOO WEE WOO" + alarm_emoji)

@bot.command()
async def repost(ctx):
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

@bot.command()
async def favorite(ctx, mention):
    if ctx.message.author.id == owen_id:
        if len(ctx.message.mentions) > 1:
            await ctx.send("fuck you only one favorite allowed")
        else:
            mention = int(mention[2:-1])
            global cur_fav
            cur_fav = mention
    else:
        await ctx.send("fuck you only owen gets to favorite")

### REMOVED COMMANDS ###

img_dict = create_dict()

cur_fav = 0

data = json.load(open("info.json"))
token = data["token"]
phrase = data["phrase"]
owen_id = int(data["id"]["owen_id"])
owenbot_id = int(data["id"]["owenbot_id"])
general_ch_id = int(data["channel"]["general"])

heart_emoji = data["unicode"]["emoji"]["heart_emoji"]
alarm_emoji = data["unicode"]["emoji"]["alarm_emoji"]
policecar_emoji = data["unicode"]["emoji"]["policecar_emoji"]
lol = data["unicode"]["kek"]

bot.run(token)
