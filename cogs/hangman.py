from ast import alias
import discord
import random
from discord.ext import commands, tasks
from discord import option

### TODO:
#   - change the info ui to something more useful

class hangman(commands.Cog):
    #########################################################################################
    #                           Hangman Minigame                                            #
    #########################################################################################
    def __init__(self, client):
        self.client = client
        # Checks if a game is currently playing
        self.hangmanQuiz = False
        # Holds the word from the list in hangmanInit
        self.hangmanWord = None
        # Success condition
        self.hangmanWin = False
        self.health = 6

    # A 5x4 matrix ASCII art
    # List goes from 0 HP to 6 HP,
    # Updating the UI as HP decreases
    commands.hpUI =  ["Γ--| \n| O \n|  -|-\n| / \\ ",
                "Γ--| \n|  O \n|  -| \n| / \\ ",
                "Γ--| \n|  O \n|     | \n| / \\ ",
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
    @commands.slash_command(name='hangman', description="Play Hangman with Vert!")
    async def hangmanInit(self, ctx):
        '''
        #### Play Hangman with Vert!
        Usage: `/hangman` or `/hm`

        Use `/hmg` to guess a letter or phrase. If the guess is wrong, regardless if it was a letter or phrase, you only lose one hp.
        '''
        # Stops if there is a game currently underway
        if (self.hangmanQuiz):
            await ctx.respond(embed=discord.Embed(title="Hangman", description="There is a gaming ongoing!", color = 0x00ff00))
            return

        self.hangmanWord = random.choice(commands.words)
        self.hangmanQuiz = True

        commands.currentWord = ["\\_"] * len(self.hangmanWord)
              
        for x in range(len(self.hangmanWord)):
            if self.hangmanWord[x] == " ":
                commands.currentWord[x] = " "
                continue

        await self.hangmanCanvasUpdate(ctx, "-")

    # Command that player uses to guess
    @commands.slash_command(name='hmg', aliases=['hmg', 'hmguess'])
    @option("message", description="Usage: <letter or phrase> to guess. Hangman game must be playing.", required=True)
    async def hangmanGuessLetter(self, ctx, *, message: str):

        if not self.hangmanQuiz:
            await ctx.respond(embed=discord.Embed(title="Hangman", description="There is no game currently ongoing!", color = 0x00ff00))
            return
       
        guess = str.lower(message)

        # DEBUG: Force Game Over
        if guess == "forcelose":
            self.health = 0
            await self.hangmanCanvasUpdate(ctx, "-")
            return

        if guess in str.lower(self.hangmanWord):
            await self.hangmanCanvasUpdate(ctx, guess)
            return
        
        # If letter is not in word, reduce hp
        self.health -= 1
        await self.hangmanCanvasUpdate(ctx, "-")

    @commands.slash_command(name='hmquit', aliases=['hmquit', 'hmq'])
    async def hangmanQuit(self, ctx):
        embed = discord.Embed(title="You bailed. Quitter.", color = 0x00ff00)
        embed.add_field(name="The answer was: ", value=self.hangmanWord)
        await ctx.respond(embed=embed)
        commands.hangmanQuit = False
        await self.hangmanReset()

    # Updates the current UI with ASCII
    async def hangmanCanvasUpdate(self, ctx, guess):
        hangmanUI = discord.Embed(title="Hangman", color = 0x00ff00)
        hangmanUI.add_field(name="Mr. Hang", value=await self.hangmanHealthUI(self))
        hangmanUI.add_field(name="Helpful Info", value="Do /hmg to guess a letter!\n\n(You can do either one letter or phrase)")
        hangmanUI.add_field(name="Word UI", value=await self.hangmangWordUpdate(self, guess), inline=False)
        
        # Lose Scenario
        if self.health <= 0:
            hangmanUI.clear_fields()
            hangmanUI.add_field(name="Mr. Hang", value=await self.hangmanHealthUI(self))
            hangmanUI.add_field(name="Game Over", value="You lost! Try harder loser")
            hangmanUI.add_field(name="The word was:", value=self.hangmanWord)
            await self.hangmanReset()

        # Win Scenario
        elif self.hangmanWin:
            hangmanUI.clear_fields()
            hangmanUI.add_field(name="Congration", value="You won! You are totally based and stuff!")
            await self.hangmanReset()

        hangmanUI.set_footer(text=commands.versionControl)
        await ctx.respond(embed=hangmanUI)

    async def hangmanReset(self):
        self.hangmanQuiz = False
        self.health = 6
        commands.currentWord = [None]
        self.hangmanWin = False

    async def hangmanHealthUI(self, ctx):
        return commands.hpUI[self.health]
    
    # Updates the current mystery word with all applied letters.
    async def hangmangWordUpdate(self, ctx, guess):
        for counter in range(len(guess)):
            for x in range (len(commands.currentWord)):
                if guess[counter] == str.lower(self.hangmanWord[x]):
                    commands.currentWord[x] = self.hangmanWord[x]

        toString = ''.join(str(x) for x in commands.currentWord)
        if toString == self.hangmanWord:
            self.hangmanWin = True
        return toString

#Cog stuff from src that does stuff so I can make stuff so I can do stuff
def setup(client):
    client.add_cog(hangman(client))