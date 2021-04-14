import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

#Usesrs must put this before imputing a command
client = commands.Bot(command_prefix = '--', help_command=None)

#auto loads all our cogs on startup
for cog_filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Connects to the server
@client.event
async def on_connect():
  #Prints to the console
  print('We have connected, please hold on til we get ready.'.format(client))

#Bot is ready to do stuff
@client.event
async def on_ready():
  #Prints to the console
  print('We have logged in as {0.user}'.format(client))

  #sets the status of the bot
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Michael Reeves"))

#Function runs whenever a message is outputted onto the server [it reads shit]
@client.event
async def on_message(message):
#Ignore any mesage that the bot sends
  if message.author == client.user:
    return

#Prevents collision events from both on_message() and commands
#Without this, commands may not work
  await client.process_commands(message)

#When the bot leaves or dies somehow
@client.event
async def on_disconnect():
    print('It seems that I have disconnected somehow.')

#Tells the version of the bot
@client.command(name='version')
async def version(context):   
    #A fun embed
    versionEmbed = discord.Embed(title="About:", description="A fun Vert bot.", color=0x00ff00)
    versionEmbed.add_field(name="Version Code: ", value="v1.0.2", inline=False)
    versionEmbed.add_field(name="Date Released:", value="4/11/2021", inline=False)
    versionEmbed.add_field(name="Latest Updated:", value="4/12/2021", inline=False)
    versionEmbed.set_author(name="Moonlite-S", icon_url="https://i.imgur.com/Uu5LlrJ.png")
    versionEmbed.set_footer(text="Ara Ara~")
    versionEmbed.set_thumbnail(url="https://i.imgur.com/5fQopQr.png")

    await context.message.channel.send(embed=versionEmbed)

    ################            Misc Commands           ###################

#Simply replies hello with the user who said it
@client.command(name='hello')
async def hello(context):
    user = str(context.author)

    hiEmb = discord.Embed(title=f"Hello, {user[:-5]}!", color=0x00ff00)
    await context.message.channel.send(embed=hiEmb)

#A reee button? I don't fucking know
@client.command(name='reee')
async def reee(ctx):
    reBed = discord.Embed(title="REEEEEEEEEEEEEEEEEEEEEEEEEEEE", color=0x00ff00)
    await ctx.message.channel.send(embed=reBed)

#Loads up the env file to pass the token
load_dotenv()
client.run(os.getenv('DISCORD_TOKEN'))