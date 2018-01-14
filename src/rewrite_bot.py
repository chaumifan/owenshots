import random
import ngram
import json
import textwrap
import os
from PIL import Image, ImageDraw, ImageFont

import discord
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


@bot.command(description="Description of echo")
async def echo(ctx, *args):
    """Bot will repeat anything said."""
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

@bot.command()
async def eightballchau(ctx):
    """Call upon eight ball Chau. Can also use !8ballchau."""
    await ctx.send(random.choice(phrase))

@bot.command()
async def kek(ctx):
    """Sends kekeke in Korean characters."""
    await ctx.send(lol)

@bot.command()
async def wagecuckalarm(ctx):
    """Notifies wage cucks to go to sleep."""
    await ctx.send(alarm_emoji + "WEE WOO WEE WOO" + alarm_emoji)
    await ctx.send(alarm_emoji + "WAGE CUCKS GO TO SLEEP" + alarm_emoji)
    await ctx.send(alarm_emoji + "WEE WOO WEE WOO" + alarm_emoji)

@bot.command()
async def repost(ctx):
    """Alerts others when something is reposted."""
    await ctx.send(policecar_emoji + 
            "repost alert repost alert weewooweewooweewoo" +
            policecar_emoji)
    await ctx.send(policecar_emoji +
            "put the memes down and step away from the computer" +
            policecar_emoji)

@bot.command()
async def addimg(ctx, name, image_link):
    """Adds an image as a command."""
    with open("image.info", "a") as f:
        f.write(name + " " + image_link)
    img_dict[name] = image_link

@bot.command()
async def listimg(ctx):
    """Lists images. Call using !<name>"""
    s = ""
    for key in img_dict:
        s = s + key + ", "
    s = s[:-2]
    await ctx.send(s)

@bot.command()
async def favorite(ctx, mention):
    """Allows Owen to choose his current favorite."""
    if ctx.message.author.id == owen_id:
        if len(ctx.message.mentions) > 1:
            await ctx.send("fuck you only one favorite allowed")
        else:
            mention = int(mention[2:-1])
            global cur_fav
            cur_fav = mention
    else:
        await ctx.send("fuck you only owen gets to favorite")

@bot.command(description=
        "Uses ngram library with data scraped from Facebook and Discord")
async def mimic(ctx, word, num_words=0):
    """Mimics Owen given a starting word."""
    sentence = ngram.ngram(counts, word, num_words)
    await ctx.send(sentence)

@bot.command()
async def spoiler(ctx, *, text: str):
    """Creates a mouseover gif of the spoiler text."""
    # Source: 
    # https://github.com/flapjax/FlapJack-Cogs/blob/master/spoiler/spoiler.py
    temp_filepath = "spoiler/"
    line_length = 60
    margin = (5,5)
    font = "spoiler/UbuntuMono-Regular.ttf"
    font_size = 14
    font_color = 150

    message = ctx.message
    author = message.author.display_name


    title = "Mouseover to reveal spoiler"
    if title == ''.join(text):
        await ctx.send("Nice try :|")
        return

    try:
        await message.delete()
    except discord.errors.Forbidden:
        await ctx.send("I require the 'manage messages' permission "
                           "to hide spoilers!")

    try:
        fnt = ImageFont.truetype(font, font_size)
    except OSError:
        await ctx.send("I couldn't load the font file. Try "
                           "reinstalling via the downloader cog, or "
                           "manually place `UbuntuMono-Regular.ttf` "
                           "in `/data/spoiler/`")
        return

    spoil_lines = []
    for line in text.splitlines():
        spoil_lines.extend(textwrap.wrap(line, line_length,
                                         replace_whitespace=False))

    width = fnt.getsize(title)[0] + 50
    height = 0

    for line in spoil_lines:
        size = fnt.getsize(line)
        width = max(width, size[0])
        height += size[1] + 2

    width += margin[0]*2
    height += margin[1]*2

    spoils = '\n'.join(spoil_lines)

    spoil_img = [new_image(width, height) for _ in range(2)]
    spoil_text = [title, spoils]

    for img, txt in zip(spoil_img, spoil_text):
        canvas = ImageDraw.Draw(img)
        try:
            canvas.text(margin, txt, font=fnt, fill=font_color,
                        spacing=4)
        except TypeError:
            canvas.text(margin, txt, font=fnt, fill=font_color)

    path = temp_filepath + ''.join(random.choice(
               '0123456789ABCDEF') for i in range(12)) + ".gif"

    spoil_img[0].save(path, format="GIF", save_all=True,
                      append_images=[spoil_img[1]],
                      duration=[0, 0xFFFF], loop=0)
    content = "**" + author + "** posted this spoiler:"
    
    f = discord.File(path)
    await ctx.send(file=f, content=content)
    os.remove(path)

def new_image(width, height):
    return Image.new("L", (width, height), bg_color)


### REMOVED COMMANDS ###

img_dict = create_dict()
counts = ngram.ngram_init()

cur_fav = 0

bg_color = 20

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
