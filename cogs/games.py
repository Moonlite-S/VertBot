import discord
import random
from cogs.database.animeData import *
from discord.ext import commands, tasks

# Games are fun
class games(commands.Cog):

    def __init__(self, client):
        self.client = client

    #########################################################################################
    #                               8Ball Minigame                                          #
    #########################################################################################

    @commands.slash_command(name='8ball', description="Ask a question and an 8Ball will guide you with an answer.")
    async def ball(self, ctx, *, message: str):
        '''
        #### Ask Vert a question and she will answer with her 8Ball!
        Usage: `--8ball <question>?`

        The input must have a question mark. Vert will answer your question with a random response. If no question is asked, Vert will ask you to ask her a question.
        '''
        responses = [
            "Absolutely not.", "Maybe so.", "Fortune says yes.",
            "Try again later.", "Die in a fire.", "My ara senses say yes.",
            "Cry more.", "Your luck has run out.", "No.", "L + ratio", "LMAO"
            ]

        await self.ballCheckAndAnswerQuestion(ctx, responses, message)
    
    #       8Ball Helper Functions      #
    #Checks if the user inputted a questions, then answers said question if true
    #with a random response
    async def ballCheckAndAnswerQuestion(self, ctx, response, message):
        if "?" in message:
            ballEmb = discord.Embed(color = 0x00ff00, description = random.choice(response))
            await ctx.respond(embed=ballEmb)
        else:
            ballEmb = discord.Embed(title="Ask me a question, please.", color = 0x00ff00)
            await ctx.respond(embed=ballEmb)

    #########################################################################################
    #                       Rock, Paper, Scissors Minigame                                  #
    #########################################################################################

    @commands.slash_command(name='rps', description="Play Rock, Paper, Scissors with Vert!")
    async def rps(self, ctx, *, message: str):
        '''
        #### Play Rock, Paper, Scissors with Vert!
        Usage: `--rps <rock, paper, scissors>`

        Vert will randomly choose rock, paper, or scissors and will respond with your input.
        '''
        trio = ["rock", "paper", "scissors"]

        bot_input = random.choice(trio)

        win_responses = [f"Hah, I picked {bot_input}.", f"Ohoho, you lucked out. I picked {bot_input}!",
                         f"Looks like victory goes to me! Go team {bot_input}!", f"How unfortunate for you; I picked {bot_input}."]

        loss_responses = [f"Oh no, I picked {bot_input}. I lost...", f"I picked {bot_input}.. How could I lose?", f"How could this be? I thought I could win with {bot_input}..",
                          f"Oh man, I picked {bot_input}.. I guess you win.."]

        tie_responses = [f"Oh, I guess we tied.",f"Interesting, we chose the same thing.",f"Ah great minds think alike. I also picked {bot_input}",
                         f"It seems that we have tied."]

        user = message

        await self.rpsCheckWhoWins(user, bot_input,loss_responses, win_responses, tie_responses, ctx)
    
    # Rock, Paper, Scissors Helper Functions
    # Checks if user inputed valid word, then calculate who wins
    async def rpsCheckWhoWins(self, user_in, bot_in, loss, win, tie, ctx):
        rpsEmbed = discord.Embed(color=0x00ff00, description="")
        user_in = str.lower(user_in)

        rpsEmbed.add_field(name="You chose:", value=user_in, inline=False)

        #Checks if user has any of the three choices allowed
        if user_in == "rock" or user_in == "paper" or user_in == "scissors":
            #Tie Check
            if user_in == bot_in:
                rpsEmbed.description=random.choice(tie)
                await ctx.respond(embed=rpsEmbed)
            #Checks to see if the bot wins
            elif (user_in == "rock" and bot_in == "paper") or (user_in == "paper" and bot_in == "scissors") or (user_in == "scissors" and bot_in == "rock"):
                rpsEmbed.description=random.choice(win)
                await ctx.respond(embed=rpsEmbed)
            #This should mean that the user wins
            else:
                rpsEmbed.description=random.choice(loss)
                await ctx.respond(embed=rpsEmbed)

        #if the user inputs something else other than rock, paper, or scissors
        else:
             rpsEmbed.description="You must put either rock, paper, or scissors."
             await ctx.respond(embed=rpsEmbed)


#Cog stuff from src that does stuff so I can make stuff so I can do stuff
def setup(client):
    client.add_cog(games(client))


