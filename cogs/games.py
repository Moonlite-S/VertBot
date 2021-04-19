import discord
import asyncio
import random
from cogs.database.animeData import *
from discord.ext import commands, tasks

#Games are fun
class games(commands.Cog):

    def __init__(self, client):
        self.client = client

    #8Ball Minigame Command
    @commands.command(name='8ball', aliases=["8Ball"])
    async def ball(self, ctx):
        responses = [
            "Absolutely not.", "Maybe so.", "Fortune says yes.",
            "Try again later.", "Die in a fire.", "My ara senses say yes.",
            "Cry more.", "Your luck has run out.", "No."
            ]

        await self.ballCheckAndAnswerQuestion(ctx, responses)
    
    #       8Ball Helper Functions      #
    #Checks if the user inputted a questions, then answers said question if true
    #with a random response
    async def ballCheckAndAnswerQuestion(self, ctx, response):
        if "?" in ctx.message.content:
            ballEmb = discord.Embed(color = 0x00ff00, description = random.choice(response))
            await ctx.channel.send(embed=ballEmb)
        else:
            ballEmb = discord.Embed(title="Ask me a question, please.", color = 0x00ff00)
            await ctx.channel.send(embed=ballEmb)

    #Rock, Paper, Scissors Minigame Command
    @commands.command(name='rps', aliases=['RPS'])
    async def rps(self, ctx):
        trio = ["rock", "paper", "scissors"]

        bot_input = random.choice(trio)

        win_responses = [f"Hah, I picked {bot_input}.", f"Ohoho, you lucked out. I picked {bot_input}!",
                         f"Looks like victory goes to me! Go team {bot_input}!", f"How unfortunate for you; I picked {bot_input}."]

        loss_responses = [f"Oh no, I picked {bot_input}. I lost...", f"I picked {bot_input}.. How could I lose?", f"How could this be? I thought I could win with {bot_input}..",
                          f"Oh man, I picked {bot_input}.. I guess you win.."]

        tie_responses = [f"Oh, I guess we tied.",f"Interesting, we chose the same thing.",f"Ah great minds think alike. I also picked {bot_input}",
                         f"It seems that we have tied."]

        user = ctx.message.content[6:]

        await self.rpsCheckWhoWins(user, bot_input,loss_responses, win_responses, tie_responses, ctx)
    
    #       Rock, Paper, Scissors Helper Functions      #
    #Checks if user inputed valid word, then calculate who wins
    async def rpsCheckWhoWins(self,user_in, bot_in, loss, win, tie, ctx):
        rpsEmbed = discord.Embed(color=0x00ff00, description="")
        #Checks if user has any of the three choices allowed
        if user_in == "rock" or user_in == "paper" or user_in == "scissors":
            #Tie Check
            if user_in == bot_in:
                rpsEmbed.description=random.choice(tie)
                await ctx.channel.send(embed=rpsEmbed)
            #Checks to see if the bot wins
            elif (user_in == "rock" and bot_in == "paper") or (user_in == "paper" and bot_in == "scissors") or (user_in == "scissors" and bot_in == "rock"):
                rpsEmbed.description=random.choice(win)
                await ctx.channel.send(embed=rpsEmbed)
            #This should mean that the user wins
            else:
                rpsEmbed.description=random.choice(loss)
                await ctx.channel.send(embed=rpsEmbed)

        #if the user inputs something else other than rock, paper, or scissors
        else:
             rpsEmbed.description="You must put either rock, paper, or scissors."
             await ctx.channel.send(embed=rpsEmbed)

    #Hangman Minigame Command
    @commands.command(name='hangman', aliases=['hm'])
    async def hangman(ctx, input):
        pass

    #Local variables For animeQuiz
    #anim is an Object from anime class in animeData.py
    commands.animeQuizOn = False
    commands.anim = None

    #Anime Quiz Minigame Command
    @commands.command(name='animequiz', aliases=['aq'])
    async def animequiz(self, ctx):
        #Checks to see if there's a quiz minigame ongoing
        if commands.animeQuizOn == False:
            await self.animQuizInitialization(ctx)
        else:
            animInGameEmbed = discord.Embed(title="There is a game ongoing!", color=0x00ff00)
            await ctx.channel.send(embed=animInGameEmbed)
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
            animEmbedTime.description = f"The anime was {commands.anim.getName()}"
            animEmbedTime.set_image(url=commands.anim.getPicture())
            await ctx.channel.send(embed=animEmbedTime)
            commands.animeQuizOn = False
        else:
            return

    #Gives a hint if no one has answered it correctly yet
    async def animQuizGiveHint(self, ctx):
        if commands.animeQuizOn:
            animEmbedTime = discord.Embed(title="Here's a hint:", color=0x00ff00, description="")
            animEmbedTime.description = commands.anim.askHint()
            await ctx.channel.send(embed=animEmbedTime)

    #Gives a picture hint
    async def animQuizGivePicHint(self, ctx):
        if commands.animeQuizOn:
            animEmbedTime = discord.Embed(title="Here's a hint:", color=0x00ff00, description="")
            animEmbedTime.set_image(url=commands.anim.askPicHint())
            await ctx.channel.send(embed=animEmbedTime)

    #Initializes the quiz to start
    async def animQuizInitialization(self, ctx):
        #Turns on the quiz minigame
        commands.animeQuizOn = True;

        #Gets a random anime object from the catalog
        commands.anim = random.choice(animList)

        #Start the quiz by giving the description of a random anime
        animEmbed = discord.Embed(title="What anime is this?", color=0x00ff00, description="")
        animEmbed.description = commands.anim.getDescription()
        await ctx.channel.send(embed=animEmbed)
        return True



#Cog stuff from src that does stuff so I can use stuff
def setup(client):
    client.add_cog(games(client))


