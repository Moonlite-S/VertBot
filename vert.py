import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

client = commands.Bot(command_prefix = 'V!')

@client.event
async def on_connect():
  #Prints to the console
  print('We have connected, please hold on til we get ready.'.format(client))

#Bot is ready to do stuff
@client.event
async def on_ready():
  #Prints to the console
  print('We have logged in as {0.user}'.format(client))

#Update() function [do shit]
@client.event
#Function runs whenever a message is outputted onto the server [it reads shit]
async def on_message(message):
  global general_channel

#Ignore any mesage that the bot sends
  if message.author == client.user:
    return

#Prevents collision events from both on_message() and commands
  await client.process_commands(message)

#When the bot leaves or dies somehow
@client.event
async def on_disconnect():
    print('It seems that I have disconnected somehow.')

######################      Commands BITCH      #########################

@client.command(name='version')
async def version(context):   
    #A fun embed
    versionEmbed = discord.Embed(title="About:", description="A fun Vert bot.", color=0x00ff00)
    versionEmbed.add_field(name="Version Code: ", value="v1.0.0", inline=False)
    versionEmbed.add_field(name="Date Released:", value="4/11/2021", inline=False)
    versionEmbed.set_author(name="Moonlite-S")
    versionEmbed.set_footer(text="Ara Ara")

    await context.message.channel.send(embed=versionEmbed)


#Loads up the env file to pass the token
load_dotenv()
client.run(os.getenv('DISCORD_TOKEN'))