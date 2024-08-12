from discord.ext import commands
import discord
import random
from discord import option

'''TODO:
- So far it's single player, but eventually I want to this minigame used for multiple players at once
    (maybe create a class for each player)
- Since we have slash commands, we could make the hit and update reaction based?
'''

class blackjack(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.isOngoing = False
        self.deck: list[str] = ["D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","DA",
                    "C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","CA",
                    "S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","SA",
                    "H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","HA"]
        self.player_hand: list[str] = []
        self.vert_hand: list[str] = []
        self.vert_win_responses = ["Ara ara, There was only ever one outcome.", "Victory is mine!"]
        self.vert_lose_responses = ["How could this be? I thought I could win...", "I guess you win..."]
    
    @commands.slash_command(name="blackjack", description="Play Blackjack with Vert!")
    @option("hitorpass", description="Use 'hit' or 'pass' or 'quit'. To start the game, use this command with no arguements.", required=False)
    async def blackjackInit(self, ctx, *, hitorpass:str):
        ''' ### Initializes Blackjack mini-game. 
        The game is played casual-styled. No chips or betting.

        First both are dealt two cards and then, the player goes first. 
        The player can hit as many times before they pass. Then the game is finalized on Vert's turn.
        '''

        await self.messageValidation(ctx, hitorpass)

    # Helper Functions #
    
    async def messageValidation(self, ctx, message: str):
        '''This decides on what to do based on response'''
        if not message and not self.isOngoing:
            return await self.blackjackStartGame(ctx)

        if not self.isOngoing:
            return await self.gameOngoingEmbed(ctx)
        
        # Check Message
        if message.lower().strip() == "hit":
            await self.blackjackHit(ctx)
        elif message.lower().strip() == "pass":
            await self.blackjackPass(ctx)
        elif message.lower().strip() == "quit":
            await self.blackjackQuit(ctx)
    
    async def blackjackStartGame(self, ctx):

        self.isOngoing = True
        self.resetGame()
        self.drawInitCards()
        await self.showHand(ctx)
    
    async def blackjackQuit(self, ctx):
        ''' Quits the game manually. '''
        
        self.resetGame()
        self.isOngoing = False
        embed = discord.Embed(title="Blackjack Ended", description="You quit the game. Quitter.", color = 0x00ff00)
        await ctx.respond(embed=embed)

    async def blackjackHit(self, ctx):
        ''' Player hits. '''

        self.drawCard(self.player_hand)

        if self.calculateHand(self.player_hand) > 21:
            self.isOngoing = False
            await self.calculateWinner(ctx)
        else:
            self.vertHit()
            await self.showHand(ctx)


    async def blackjackPass(self, ctx):
        ''' Player passes on drawing a card. '''

        self.vertHit()
        await self.calculateWinner(ctx)
        
    def drawInitCards(self):
        ''' Draws the initial two cards for both the player and Vert. '''
        for _ in range(2):
            self.drawCard(self.player_hand)
            self.drawCard(self.vert_hand)

    async def showHand(self, ctx):
        ''' Shows only player's hand as an embed message to channel. '''
        embed = discord.Embed(title="Blackjack", description="Your hand:", color = 0x00ff00)
        embed.add_field(name="Your Hand:", value=self.printHand(self.player_hand))
        embed.add_field(name="Value:", value=self.calculateHand(self.player_hand))
        embed.add_field(name="Hit or Pass?", value="Type /blackjack 'hit' or 'pass' to continue.", inline=False)
        await ctx.respond(embed=embed)

    def resetGame(self):
        ''' Resets the game variables. '''
        self.deck = ["D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","DA",
                    "C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","CA",
                    "S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","SA",
                    "H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","HA"]
        self.player_hand = []
        self.vert_hand = []

    def vertHit(self):
        ''' ### Calculates the value of the hand and decides whether to hit or not. '''

        rng = random.randint(1, 100)
        vert_hand_value = self.calculateHand(self.vert_hand)

        if vert_hand_value < 12:
            self.drawCard(self.vert_hand)
        elif vert_hand_value < 16:
            if rng <= 80:
                self.drawCard(self.vert_hand)
        elif vert_hand_value < 18:
            if rng <= 40:
                self.drawCard(self.vert_hand)
        elif vert_hand_value < 20:
            if rng <= 10:
                self.drawCard(self.vert_hand)
            return
        else:
            return
        
        self.vertHit()

    def drawCard(self, hand: list[str]):
        ''' Randomly pops a card from the deck list. Hand is an array of strings that holds the type and num of card  '''
        card = self.deck.pop(random.randint(0, len(self.deck) - 1))
        hand.append(card)

    def calculateHand(self, hand: list[str]) -> int:
        ''' Calculates the hand's value of given argument. 
        2-10 = simple
        J, Q, K = 10
        A = 11, unless the hand is over 21, then it's 1.
        '''

        if len(hand) == 0:
            print("Hand is empty. This should not have happened.")
            commands.on_command_error()
            return 0
        
        value = 0
        ace_check = (False, 0) # Keeps track if there is an Ace and the number of Aces in hand.

        for card in hand:
            if card[1] == "A":
                value += 11
                ace_check = (True, ace_check[1] + 1)
                
            elif card[1] in ["J", "Q", "K", "1"]:
                value += 10
            else:
                value += int(card[1])

        for _ in range(ace_check[1]):
            if ace_check[0] and value > 21:
                value -= 10

        return value

    async def gameOngoingEmbed(self, ctx):
        ''' Checks to see if a game is currently running. If not, sends an Embed about it. '''
        if not self.isOngoing:
            embed = discord.Embed(title="Blackjack", description="There is no game ongoing!", color = 0x00ff00)
            await ctx.respond(embed=embed)

    async def calculateWinner(self, ctx):
        ''' Calculates the winner. '''

        self.isOngoing = False

        vert_hand_value = self.calculateHand(self.vert_hand)
        player_hand_value = self.calculateHand(self.player_hand)

        if player_hand_value > 21:
            await self.embedResults(ctx, 'lose')
        elif vert_hand_value > 21 or player_hand_value > vert_hand_value:
            await self.embedResults(ctx, 'win')
        elif player_hand_value == vert_hand_value:
            await self.embedResults(ctx, 'tie')
        else:
            await self.blackjackLose(ctx)

    async def blackjackWin(self, ctx):
        ''' The player wins. '''
        embed = await self.embedResults(ctx, 'win')
        await ctx.respond(embed=embed)

    async def blackjackLose(self, ctx):
        ''' The player loses. '''
        embed = await self.embedResults(ctx, 'lose')
        await ctx.respond(embed=embed)

    async def embedResults(self, ctx, result: str):
        embed = discord.Embed(title="Blackjack Result:", color = 0x00ff00)
        embed.add_field(name="Your Hand:", value=self.printHand(self.player_hand))
        embed.add_field(name="Value:", value=self.calculateHand(self.player_hand))
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="Vert's Hand:", value=self.printHand(self.vert_hand))
        embed.add_field(name="Value:", value=self.calculateHand(self.vert_hand))

        if result == 'win':
            embed.add_field(name="Vert:", value=random.choice(self.vert_lose_responses), inline=False)
            embed.description = "You win!"
        elif result == 'lose':
            embed.add_field(name="Vert:", value=random.choice(self.vert_win_responses), inline=False)
            embed.description = "You lose!"
        elif result == 'tie':
            embed.add_field(name="Vert:", value="It's a tie!", inline=False)
            embed.description = "It's a tie!"
        else:
            print("Invalid result. Something went wrong")
            embed.add_field(name="SOMETHING HAPPENED", value="NOTHING GOOD")

        await ctx.respond(embed=embed)

    def printHand(self, hand: list[str]):
        return f"{(', '.join(hand))}"
    
#Cog stuff from src that does stuff so I can make stuff so I can do stuff
def setup(client):

    client.add_cog(blackjack(client))

