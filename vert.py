import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

client = commands.Bot(command_prefix = '#')

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

#Ignore any mesage that the bot sends
  if message.author == client.user:
    return

#Channel Access Variables (Based on my personal server)
  general_channel = client.get_channel(830170824115224577)


#Simple response by saying hello
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')


#Loads up the env file to pass the token
load_dotenv()
client.run(os.getenv('DISCORD_TOKEN'))