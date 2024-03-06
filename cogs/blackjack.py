from discord.ext import commands, tasks
import discord
import random

'''TODO:
- Setup game variables
- Setup player input
- So far it's single player, but eventually I want to this minigame used for multiple players at once
- "How to know when to stop?" When both the player and Vert don't hit in the same turn, the game ends on Vert's turn.
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
    
    @commands.command(name="blackjack")
    async def blackjackInit(self, ctx):
        ''' Initializes Blackjack mini-game. '''
        if self.isOngoing:
            await ctx.channel.send(embed=discord.Embed(title="Blackjack", description="There is a game ongoing!", color = 0x00ff00))
            return
        
        isOngoing = True

        self.resetGame()

        self.blackjackHit(ctx)
        self.blackjackHit(ctx)
        self.vertHit(ctx)
        self.vertHit(ctx)

        self.showHands(ctx)

    @commands.command(name="blackjackHit", aliases=["hit"])
    async def blackjackHit(self, ctx):
        ''' Player hits. '''

        # Game Validation
        if not self.isOngoing:
            embed = discord.Embed(title="Blackjack", description="There is no game ongoing!", color = 0x00ff00)
            await ctx.channel.send(embed=embed)
            return

        self.drawCard(self.player_hand)

        if self.calculateHand(self.player_hand) > 21:
            self.calculateWinner(ctx)
        else:
            self.vertHit(ctx)
            self.showHands(ctx)

    @commands.command(name="blackjackPass", aliases=["pass"])
    async def blackjackPass(self, ctx):
        ''' Player passes on drawing a card. '''

        # Game Validation
        if not self.isOngoing:
            embed = discord.Embed(title="Blackjack", description="There is no game ongoing!", color = 0x00ff00)
            await ctx.channel.send(embed=embed)
            return
        
        self.vertHit(ctx)
        self.showHands(ctx)

    @commands.command(name="blackjackQuit", aliases=["quit"])
    async def blackjackQuit(self, ctx):
        ''' Quits the game manually. '''
        
        # Game Validation
        if not self.isOngoing:
            embed = discord.Embed(title="Blackjack", description="There is no game ongoing!", color = 0x00ff00)
            await ctx.channel.send(embed=embed)
            return
        
        self.resetGame()
        self.isOngoing = False
        embed = discord.Embed(title="Blackjack Ended", description="You quit the game. Quitter.", color = 0x00ff00)
        await ctx.channel.send(embed=embed)

    # Helper Functions #

    async def showHands(self, ctx):
        ''' Shows both hands as an embed message to channel. '''
        embed = discord.Embed(title="Blackjack", description="Your hand:", color = 0x00ff00)
        embed.add_field(name="Your Hand:", value=self.player_hand)
        embed.add_field(name="Vert's Hand:", value=self.vert_hand)
        ctx.channel.send(embed=embed)

    async def resetGame(self):
        ''' Resets the game variables. '''
        self.deck = ["D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","DA",
                    "C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","CA",
                    "S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","SA",
                    "H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","HA"]
        self.player_hand = []
        self.vert_hand = []

    async def vertHit(self):
        ''' ### Calculates the value of the hand and decides whether to hit or not.
        < 10 = Guaranteed hit
        10-12 = 80% chance to hit
        13-16 = 40% chance to hit
        17-20 = 10% chance to hit
        21 = No hit
        '''
        

        pass

    async def drawCard(self, hand: list[str]):
        ''' Draws a card from the deck. '''
        card = self.deck.pop(random.randint(0, len(self.deck) - 1))
        hand.append(card)

    async def calculateHand(self, hand: list[str]) -> int:
        ''' Calculates the hand's value. 
        2-10 = simple
        J, Q, K = 10
        A = 1 or 11
        '''

        if len(hand) == 0:
            print("Hand is empty. This should not have happened.")
            return 0
        
        value = 0
        ace_check = False

        # So far, this does NOT count for multiple Aces
        for card in hand:
            if card[1] == "A":
                value += 11
                ace_check = True
            elif card[1] in ["J", "Q", "K"]:
                value += 10
            else:
                value += int(card[1])

        if ace_check and value > 21:
            value -= 10

        return value

    async def calculateWinner(self):
        ''' Calculates the winner. '''

        self.isOngoing = False

        if self.calculateHand(self.vert_hand) > 21:
            self.blackjackWin()
            return
        
        elif self.calculateHand(self.player_hand) < 21 and self.calculateHand(self.player_hand) > self.calculateHand(self.vert_hand):
            self.blackjackWin()
            return
        
        else:
            self.blackjackLose()
            return

    async def blackjackWin(self, ctx):
        ''' The player wins. '''
        embed = discord.Embed(title="Blackjack Result:", description="You win!", color = 0x00ff00)
        embed.add_field(name="Your Hand:", value=self.player_hand)
        embed.add_field(name="Vert's Hand:", value=self.vert_hand)
        embed.add_field(name="Vert:", value="How could I lose?")
        await ctx.channel.send(embed=embed)
        pass

    async def blackjackLose(self, ctx):
        ''' The player loses. '''
        embed = discord.Embed(title="Blackjack Result:", description="You lose!", color = 0x00ff00)
        embed.add_field(name="Your Hand:", value=self.player_hand)
        embed.add_field(name="Vert's Hand:", value=self.vert_hand)
        embed.add_field(name="Vert:", value="Ara ara, There was only ever one outcome.")
        await ctx.channel.send(embed=embed)
        pass

#Cog stuff from src that does stuff so I can make stuff so I can do stuff
async def setup(client):
    await client.add_cog(blackjack(client))

