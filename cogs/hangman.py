from ast import alias
import discord
import random
from discord.ext import commands, tasks

### TODO:
#   - make bot delete it's previous messages to conserve space (?)
#   - fix the ASCII art on the Health UI
#   - make the word ui larger if possible
#   - change the info ui to something more useful

class hangman(commands.Cog):
    #########################################################################################
    #                           Hangman Minigame                                            #
    #########################################################################################
    def __init__(self, client):
        self.client = client

    # Checks if a game is currently playing
    commands.hangmanQuiz = False
    # Holds the word from the list in hangmanInit
    commands.hangmanWord = None
    # Success condition
    commands.hangmanWin = False
        
    commands.timer = 120
    commands.health = 6

    # A 5x4 matrix ASCII art
    # List goes from 0 HP to 6 HP,
    # Updating the UI as HP decreases
    commands.hpUI =  ["Γ--| \n| O \n|  -|-\n| / \ ",
                "Γ--| \n|  O \n|  -| \n| / \ ",
                "Γ--| \n|  O \n|     | \n| / \ ",
                "Γ--| \n|  O \n|     | \n| /  ", 
                "Γ--| \n|  O \n|     | \n|    ",
                "Γ--| \n|  O \n|     \n|    ",
                "Γ--| \n|    \n|     \n|    "]
    
    # Word list the bot will choose from
    commands.words = ["Hangman", "Microcontroller", "Ceres Fauna", "Minecraft", "Love is War",
    "Arknights", "Pokemon", "Nintendo Switch", "Twitter", "Dance Dance Revolution", "Vocaloid",
    "Hatsune Miku", "Love Live"]

    commands.currentWord = [None]

    commands.versionControl = "1.2"

    #Hangman Minigame Command
    @commands.command(name='hangman', aliases=['hm'])
    async def hangmanInit(self, ctx):
        '''
        #### Play Hangman with Vert!
        Usage: `--hangman` or `--hm`

        Use `--hmg` to guess a letter or phrase. If the guess is wrong, regardless if it was a letter or phrase, you only lose one hp.
        '''
        # Stops if there is a game currently underway
        if (commands.hangmanQuiz):
            await ctx.channel.send(embed=discord.Embed(title="Hangman", description="There is a gaming ongoing!", color = 0x00ff00))
            return

        commands.hangmanWord = random.choice(commands.words)
        commands.hangmanQuiz = True

        commands.currentWord = ["\_"] * len(commands.hangmanWord)
              
        for x in range(len(commands.hangmanWord)):
            if commands.hangmanWord[x] == " ":
                commands.currentWord[x] = " "
                continue

        await self.hangmanCanvasUpdate(ctx, "-")

    # Command that player uses to guess
    @commands.command(name='hangmanGuess', aliases=['hmg', 'hmguess'])
    async def hangmanGuessLetter(self, ctx):

        if not commands.hangmanQuiz:
            await ctx.channel.send(embed=discord.Embed(title="Hangman", description="There is no game currently ongoing!", color = 0x00ff00))
            return
       
        guess = str.lower(ctx.message.content[6:])

        # DEBUG: Force Game Over
        if guess == "forcelose":
            commands.health = 0
            await self.hangmanCanvasUpdate(ctx, "-")
            return

        if guess in str.lower(commands.hangmanWord):
            await self.hangmanCanvasUpdate(ctx, guess)
            return
        
        # If letter is not in word, reduce hp
        commands.health -= 1
        await self.hangmanCanvasUpdate(ctx, "-")

    # Updates the current UI with ASCII
    async def hangmanCanvasUpdate(self, ctx, guess):
        hangmanUI = discord.Embed(title="Hangman", color = 0x00ff00)
        hangmanUI.add_field(name="Mr. Hang", value=await self.hangmanHealthUI(self))
        hangmanUI.add_field(name="Helpful Info", value="Do --hmg to guess a letter!\n\n(You can do either one letter or phrase)")
        hangmanUI.add_field(name="Word UI", value=await self.hangmangWordUpdate(self, guess), inline=False)
        
        # Lose Scenario
        if commands.health <= 0:
            hangmanUI.clear_fields()
            hangmanUI.add_field(name="Mr. Hang", value=await self.hangmanHealthUI(self))
            hangmanUI.add_field(name="Game Over", value="You lost! Try harder loser")
            hangmanUI.add_field(name="The word was:", value=commands.hangmanWord)
            await self.hangmanReset()

        # Win Scenario
        elif commands.hangmanWin:
            hangmanUI.clear_fields()
            hangmanUI.add_field(name="Congration", value="You won! You are totally based and stuff!")
            await self.hangmanReset()

        hangmanUI.set_footer(text=commands.versionControl)
        await ctx.channel.send(embed=hangmanUI)

    async def hangmanReset(self):
        commands.hangmanQuiz = False
        commands.health = 6
        commands.currentWord = [None]
        commands.hangmanWin = False

    async def hangmanHealthUI(self, ctx):
        return commands.hpUI[commands.health]
    
    # Updates the current mystery word with all applied letters.
    async def hangmangWordUpdate(self, ctx, guess):
        for counter in range(len(guess)):
            for x in range (len(commands.currentWord)):
                if guess[counter] == str.lower(commands.hangmanWord[x]):
                    commands.currentWord[x] = commands.hangmanWord[x]

        toString = ''.join(str(x) for x in commands.currentWord)
        if toString == commands.hangmanWord:
            commands.hangmanWin = True
        return toString

#Cog stuff from src that does stuff so I can make stuff so I can do stuff
async def setup(client):
    await client.add_cog(hangman(client))