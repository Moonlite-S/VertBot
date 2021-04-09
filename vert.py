import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
#Ignore any mesage that the bot sends
  if message.author == client.user:
    return

#Simple response by saying hello
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

client.run(os.getenv('DISCORD_TOKEN'))
