import discord
import os
import asyncio
from discord.ext import commands, tasks
from dotenv import load_dotenv

#Usesrs must put this before imputing a command
client = commands.Bot(command_prefix = '--', help_command=None)

#auto loads all our cogs on startup
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        #ignore any init files
        if (filename.startswith('__')):
            break
        client.load_extension(f'cogs.{filename[:-3]}')

#Connects to the server
@client.event
async def on_connect():
  #Prints to the console
  print('We have connected, please hold on til we get ready.'.format(client))

  #sets the status of the bot
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Michael Reeves"))

#Bot is ready to do stuff
@client.event
async def on_ready():
  #Prints to the console
  print('We have logged in as {0.user}'.format(client))

#Function runs whenever a message is outputted onto the server [it reads shit]
@client.event
async def on_message(message):
    #Ignore any mesage that the bot sends
    if message.author == client.user:
        return

    #For the Anime Quiz Minigame:
    #Once the game begins, takes in inputs
    #and checks to see if its the right answer
    if (commands.animeQuizOn):
        if(commands.anim.getName().lower() == message.content.lower()):
            await animQuizWin(client, message)
            return
        #Also checks for aliases
        for alias in commands.anim.getAliases():
            if message.content.lower() == alias.lower():
               await animQuizWin(client, message)
               return

#Allows commands to operate with this event running
#(Normally, this event forbids any extra commands from running)
    await client.process_commands(message)

#When the bot leaves or dies somehow
@client.event
async def on_disconnect():
    print('It seems that I have disconnected somehow.')

    ################            Misc Commands           ###################

#Tells the version of the bot
@client.command(name='version')
async def version(context):   
    #A fun embed
    versionEmbed = discord.Embed(title="About:", description="A fun Vert bot.", color=0x00ff00)
    versionEmbed.add_field(name="Version Code: ", value="v1.0.6", inline=False)
    versionEmbed.add_field(name="Date Released:", value="4/11/2021", inline=False)
    versionEmbed.add_field(name="Latest Updated:", value="4/18/2021", inline=False)
    versionEmbed.set_author(name="Moonlite-S", icon_url="https://i.imgur.com/Uu5LlrJ.png")
    versionEmbed.set_footer(text="Ara Ara~")
    versionEmbed.set_thumbnail(url="https://i.imgur.com/5fQopQr.png")

    await context.message.channel.send(embed=versionEmbed)

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

    ################            Helper Functions           ###################

#For Anime Quiz Minigame: Outputs the winning screen
async def animQuizWin(self, ctx):
        commands.animeQuizOn = False
        animWin = discord.Embed(title=f"Hey your winnner, the anime was {commands.anim.getName()}", color=0x00ff00)
        animWin.description = commands.anim.getDescription()
        animWin.set_image(url=commands.anim.getPicture())
        await ctx.channel.send(embed=animWin)

#Loads up the env file to pass the token
load_dotenv()
client.run(os.getenv('DISCORD_TOKEN'))