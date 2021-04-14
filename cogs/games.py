import discord
import asyncio
import random
from discord.ext import commands

#Games are fun
class games(commands.Cog):

    def __init__(self, client):
        self.client = client

    #A simple 8ball
    @commands.command(name='8ball', aliases=["8Ball"])
    async def ball(ctx, msg):
        responses = [
            "Absolutely not.", "Maybe so.", "Fortune says yes.",
            "Try again later.", "Die in a fire.", "My ara senses say yes.",
            "Cry more.", "Your luck has run out.", "No."
            ]

        #Detected if it's a question [by just looking through the message
        #to see if there's a '?']
        if "?" in msg.message.content:
            ballEmb = discord.Embed(color = 0x00ff00, description = random.choice(responses))
            await msg.channel.send(embed=ballEmb)
        else:
            await msg.channel.send("Send a question, dumbass.")
    
    #A simple rock, paper, scissors battle with the bot
    @commands.command(name='rps', aliases=["RPS"])
    async def rps(ctx, input):
        trio = ["rock", "paper", "scissors"]

        bot_input = random.choice(trio)

        win_responses = [f"Hah, I picked {bot_input}.", f"Ohoho, you lucked out. I picked {bot_input}!",
                         f"Looks like victory goes to me! Go team {bot_input}!", f"How unfortunate for you; I picked {bot_input}."]

        loss_responses = [f"Oh no, I picked {bot_input}. I lost...", f"I picked {bot_input}.. How could I lose?", f"How could this be? I thought I could win with {bot_input}..",
                          f"Oh man, I picked {bot_input}.. I guess you win.."]

        tie_responses = [f"Oh, I guess we tied.",f"Interesting, we chose the same thing.",f"Ah great minds think alike. I also picked {bot_input}",
                         f"It seems that we have tied."]

        user = input.message.content[6:]

        rpsEmbed = discord.Embed(color=0x00ff00, description="")

        if user == "rock" or user == "paper" or user == "scissors":
            if user == bot_input:
                rpsEmbed.description=random.choice(tie_responses)
                await input.channel.send(embed=rpsEmbed)

            elif (user == "rock" and bot_input == "paper") or (user == "paper" and bot_input == "scissors") or (user == "scissors" and bot_input == "rock"):
                rpsEmbed.description=random.choice(win_responses)
                await input.channel.send(embed=rpsEmbed)

            else:
                rpsEmbed.description=random.choice(loss_responses)
                await input.channel.send(embed=rpsEmbed)

        #if the user inputs something else other than rock, paper, or scissors
        else:
             rpsEmbed.description="You must put either rock, paper, or scissors."
             await input.channel.send(embed=rpsEmbed)

    @commands.command(name='hangman', aliases=['hm'])
    async def hangman(ctx, input):
        pass

#Cog stuff from src that does stuff so I can use stuff
def setup(client):
    client.add_cog(games(client))


