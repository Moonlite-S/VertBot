import discord
import os
from cogs.database.animeData import *
from discord.ext import commands
from dotenv import load_dotenv

#Usesrs must put this before imputing a command
client = commands.Bot(intents=discord.Intents.all(), help_command=commands.DefaultHelpCommand())

versionControl = "2.0.1"
lastUpdated = "5/28/2024"

@client.event
async def on_connect():
    #loads all our cogs
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and not filename.startswith('__'):
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded {filename[:-3]}')
    print('We have connected, please hold on til we get ready.'.format(client))
    await client.sync_commands()

    await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity('Gaming with Neptune'))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #Ignore any mesage that the bot sends
    if message.author == client.user:
        return

    #For the Anime Quiz Minigame:
    #Once the game begins, takes in inputs
    #and checks to see if its the right answer
    if (commands.animeQuizOn):
        await animQuizCheckWin(client, message)

    #Allows commands to operate with this event running
    #(Normally, this event forbids any extra commands from running)
    await client.process_commands(message)

#When the bot leaves or dies somehow
@client.event
async def on_disconnect():
    print('It seems that I have disconnected somehow.')

    ################            Misc Commands           ###################

#Tells the version of the bot
@client.slash_command(name='version', description="Tells you the version of Vert Bot")
async def version(context):   
    #A fun embed
    versionEmbed = discord.Embed(title="About:", description="A fun Vert bot.", color=0x00ff00)
    versionEmbed.add_field(name="Version Code: ", value=f"v{versionControl}", inline=False)
    versionEmbed.add_field(name="Date Released:", value="4/11/2021", inline=False)
    versionEmbed.add_field(name="Latest Updated:", value=lastUpdated, inline=False)
    versionEmbed.add_field(name="GitHub", value="https://github.com/Moonlite-S/VertBot", inline=False)
    versionEmbed.set_author(name="Moonlite-S", icon_url="https://i.imgur.com/Uu5LlrJ.png")
    versionEmbed.set_footer(text="Ara Ara~")
    versionEmbed.set_thumbnail(url="https://i.imgur.com/5fQopQr.png")

    await context.respond(embed=versionEmbed)

#Simply replies hello with the user who said it
@client.slash_command(name='hello', description="Say hi to Vert")
async def hello(context):
    user = str(context.author.name)

    hiEmb = discord.Embed(title=f"Hello, {user}!", color=0x00ff00)
    await context.respond(embed=hiEmb)

    ################            Helper Functions           ###################

#For Anime Quiz Minigame: Outputs the winning screen
async def animQuizWin(self, ctx):
        commands.animeQuizOn = False
        animWin = discord.Embed(title=f"Hey your winnner, the anime was {animList[commands.anim]['name'][0]}", color=0x00ff00)
        animWin.description = animList[commands.anim]["desc"]
        animWin.set_image(url=animList[commands.anim]["picBanner"])
        await ctx.channel.send(embed=animWin)
        return

#For Anime Quiz Minigame: Win Checks
async def animQuizCheckWin(self, message):
    for x in animList[commands.anim]["name"]:
            if (x.lower() == message.content.lower()):
                await animQuizWin(client, message)
                return
                
#Loads up the env file to pass the token
load_dotenv()
client.run(os.getenv('DISCORD_TOKEN'))