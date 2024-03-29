import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await client.send_message(message.channel, content = "Hello!")

with open("token", "r") as f:
    token = f.readline()
client.run(token[:-1])
