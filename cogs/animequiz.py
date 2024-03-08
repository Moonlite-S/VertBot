import discord
import asyncio
import random
from cogs.database.animeData import *
from discord.ext import commands

    #########################################################################################
    #                           Anime Quiz Minigame                                         #
    #########################################################################################
    
class animequiz(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.possibleHints = []
        commands.anim = None
        commands.animeQuizOn = False

    @commands.slash_command(name='animequiz', description="Guess the anime with the worst descriptions.")
    async def animequiz(self, ctx):
        '''
        #### Test your anime knowledge with the Anime Quiz minigame!
        Usage: `--animequiz` or `--aq`

        There is no command to input responses. When the command is run, Vert will look at every message sent to the channel.
        '''

        #Checks to see if there's a quiz minigame ongoing
        if commands.animeQuizOn == False:
            await self.animQuizInitialization(ctx)
        else:
            animInGameEmbed = discord.Embed(title="There is a game ongoing!", color=0x00ff00)
            await ctx.respond(embed=animInGameEmbed)
            return

        #range(n) where n is the maximum amount of hints given
        for i in range(3):
            await self.animWaitAndCheckQuiz(20) 
            #Show a picture as the last hint
            if i == 2:
                await self.animQuizGivePicHint(ctx)
                break
            await self.animQuizGiveHint(ctx)

        await self.animWaitAndCheckQuiz(20)
        await self.animQuizFail(ctx)
    
    #       Anime Quiz Helper Functions     #
    #Checks every half a second to see if the quiz is done
    #If it is, just reset. (Time = seconds * 2)
    async def animWaitAndCheckQuiz(self, time):
        for j in range(time):
            if commands.animeQuizOn:
                await asyncio.sleep(0.5)
            else:
                return

    #If no one gets the answer, close quiz and reveal answer
    async def animQuizFail(self, ctx):
        if commands.animeQuizOn:
            animEmbedTime = discord.Embed(title="You ran outta time, sucker", color=0x00ff00)
            animEmbedTime.description = f"The anime was {animList[commands.anim]['name'][0]}"
            animEmbedTime.set_image(url=animList[commands.anim]["picBanner"])
            await ctx.respond(embed=animEmbedTime)
            commands.animeQuizOn = False
        else:
            return

    #Gives a hint if no one has answered it correctly yet
    async def animQuizGiveHint(self, ctx):
        if commands.animeQuizOn:
            animEmbedTime = discord.Embed(title="Here's a hint:", color=0x00ff00, description="")
            hint = random.choice(self.possibleHints)
            animEmbedTime.description = hint
            self.possibleHints.remove(hint)
            await ctx.respond(embed=animEmbedTime)

    #Gives a picture hint
    async def animQuizGivePicHint(self, ctx):
        if commands.animeQuizOn:
            animEmbedTime = discord.Embed(title="Here's a hint:", color=0x00ff00, description="")
            animEmbedTime.set_image(url=random.choice(animList[commands.anim]["picHint"]))
            await ctx.respond(embed=animEmbedTime)

    #Initializes the quiz to start
    async def animQuizInitialization(self, ctx):
        #Turns on the quiz minigame
        commands.animeQuizOn = True

        #Gets a random anime object from the catalog
        commands.anim = random.choice(list(animList))

        #Gets the list of hints from the anime object
        self.possibleHints = animList[commands.anim]["hint"]

        #Start the quiz by giving the description of a random anime
        animEmbed = discord.Embed(title="What anime is this?", color=0x00ff00, description="")
        animEmbed.description = animList[commands.anim]["desc"]
        await ctx.respond(embed=animEmbed)
        return True

#Cog stuff from src that does stuff so I can make stuff so I can do stuff
def setup(client):
    client.add_cog(animequiz(client))