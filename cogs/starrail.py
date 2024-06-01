import discord
import random
from discord.ext import commands
from discord import option
from cogs.database.starrailData import *

class starrail(commands.Cog):
    # List of users that have used the command. Resets every time the bot is restarted.
    commands.userList = []

    # Local Stats for the user
    commands.fourPityCounter = 0
    commands.simcounter = 0
    commands.fiveStarPityRateUp = 0.6
    commands.totalPulls = 0
    commands.totalAmountofMoneyWasted = 0
    commands.fiveStarsPulled = 0

    commands.rarityColor = 0
    commands.tenPull = 1

    commands.isFiveStarGuaranteed = False
    commands.isFourStarGuaranteed = False

    commands.rarity = "★★★☆☆"
    commands.bannerName = ""
    commands.bannerImage = ""
    commands.imageUrl = ""

    commands.chosenTenPull = []
    commands.chosenList = []
    commands.chosenTenRarity = []
    commands.chosenPull = []

    # Standard Warping Pool
    commands.normalPull = [list(threeStarLightCones.items()), list(fourStarHeroes.items()), list(fourStarLightCones.items()), list(fiveStarHeroes.items()), list(fiveStarLightCones.items())]
    commands.fourStarPity = [list(fourStarHeroes.items()), list(fourStarLightCones.items()), list(fiveStarHeroes.items()), list(fiveStarLightCones.items())]
    commands.fiveStarPity = [list(fiveStarHeroes.items()), list(fiveStarLightCones.items())]

    # Limited Warping Pool
    commands.fourStarRateUp = []
    commands.fiveStarRateUp = []

    @commands.slash_command(name="starrailwarp", description="Simulates a summoning session for Honkai: Star Rail.")
    @option("message", description="Usage: <character_name> <lc> <10> Order does not matter. Every arguement is optional.", required=False)
    async def SWSummonSim(self, ctx, *, message: str):
        '''
        ### Simulates a summoning session for Star Rail Warp.
        Usage: `--warp <character name> <10> <lc>`

        If no arguements are provided, the default output is a single pull on the standard banner.

        Arguments are not case sensitive nor do they need to be in any specific order to work.

        `<character name>` - The name of the character you want to pull for. If a name has a space, do not include it. Use `--warpchars` to see the available characters.
         
        No character name defaults to using the Standard Warp.

        `<10>` - If you want to do a 10 pull. Otherwise, defaults to a single pull.

        `<lc>` - If you want to pull on a limited character's Light Cone banner. <character name> needs to be provided to be used. Otherwise, ignored.

        Example: `--warp imbibtorlunae 10 lc`
        '''
        versionControl = "1.6"
        gameVersion = "2.0"

        await self.resetBanner()
        charName = () # A tuple (bool, str) that holds the user's input

        # Edge case if user inputs no arguements.
        if not message:
            messageSplit = " "
        else:
            messageSplit = message.split()
        charName = await self.decodeMessage(messageSplit)
        bannerType = await self.initBannerType(charName[0], charName[1])

        user = await self.initUser(ctx.author.display_name)

        for x in range(commands.tenPull):
            await self.performSummon(bannerType)
        
        await user.setSummonResultsToStats()

        # Embed time
        embedSummon = discord.Embed(title=commands.bannerName, color=commands.rarityColor)
        embedSummon.set_thumbnail(url=commands.bannerImage)

        if commands.tenPull == 10:
            await self.setTenPullEmbed(embedSummon, user)
        else:
            await self.setSinglePullEmbed(embedSummon, user)
        
        embedSummon.set_footer(text=f"Version: {versionControl} / Patch: {gameVersion}")
        await ctx.respond(embed=embedSummon)

    @commands.slash_command(name="starrailclearpity", description="[Star Rail] Clears the pity counter for the user.")
    async def ClearPity(self, ctx):
        '''Clears the pity counter for the user.'''
        user = await self.findUser(ctx.author.display_name)
        embedClear = discord.Embed(title="Pity has been cleared!", color=0x00ff00)

        if user != "None":
            await user.clearPityFromAccount()
        else:
            embedClear = discord.Embed(title="There's no user found to clear pity!", color=0x00ff00)

        await ctx.respond(embed=embedClear)

    @commands.slash_command(name="starrailwarpchars", desciption="[Star Rail] Shows all available limited characters for the Honkai Star Rail Warp.")
    async def WarpChars(self, ctx):
        '''Shows all available limited characters for the Honkai Star Rail Warp.'''
        embedChars = discord.Embed(title="Star Rail Summon Simulator", color=0x00ff00)

        listofChars = list(limitedBanners.keys())

        embedChars.add_field(name="Available Characters", value="\n".join(listofChars), inline=False)

        await ctx.respond(embed=embedChars)

    ## Helper Functions ##
    async def performSummon(self, bannerType):
        """Simulates one summon pull depending on bannerType and user input."""
        commands.rarity = "★★★☆☆"

        # Soft Pity increases chances of getting a 5-star by 6% linearly
        if (commands.simcounter >= 75):
            commands.fiveStarPityRateUp += 6
                
        commands.simcounter += 1
        commands.fourPityCounter += 1

        await self.poolDecider()
        await self.pityDecider(bannerType)
        await self.limitedBannerDecider(bannerType)
        await self.checkRarityForColor(bannerType)
                        
        # Gather list of pulls if 10 pull
        if commands.tenPull == 10:
            commands.chosenTenPull += [commands.chosenPull]
            commands.chosenTenRarity += [commands.rarity]

        commands.totalPulls += 1
        
        # Average cost of a single pull in USD (Source: I made it the fuck up)
        commands.totalAmountofMoneyWasted += 2.65 

    async def initLimitedCharBanner(self, word):
        commands.fiveStarRateUp = [(word, limitedBanners[word]["Icon"])]
        commands.fourStarRateUp = limitedBanners[word]["Focus"]
        commands.bannerName = limitedBanners[word]["Name"]
        commands.bannerImage = limitedBanners[word]["BannerUrl"]
        return "Character"

    async def initLimitedLCBanner(self, word):
        commands.fiveStarRateUp = [(limitedBanners[word]["LightConeName"], limitedBanners[word]["LightConeUrl"])]
        commands.fourStarRateUp = limitedBanners[word]["LightConeFocus"]
        commands.bannerName = limitedBanners[word]["LightConeName"]
        commands.bannerImage = limitedBanners[word]["LightConeThumbnailUrl"]
        return "Light Cone"

    async def initStandardBanner(self):
        commands.bannerName = "Stellar Warp"
        commands.bannerImage = "https://tinyurl.com/3cbmye89"
        return "Standard"

    async def resetBanner(self):
        commands.fourStarRateUp = []
        commands.fiveStarRateUp = []

        commands.chosenTenPull = []
        commands.chosenList = []
        commands.chosenTenRarity = []

        commands.bannerName = ""
        commands.bannerImage = ""
        commands.rarity = "★★★☆☆"
        commands.imageUrl = ""

        commands.rarityColor = 0
        commands.tenPull = 1

    async def decodeMessage(self, messageSplit):
        """
        ### Decodes the input from user to decide how the simulation will be ran.
        Input:
            :messageSplit: list[str]
        Output:
            :tuple: ('bool' : Light Cone Trigger, 'str' : Character Name)
        """
        charName = ""
        lightConeTrigger = False

        # Checks message for key words
        for word in messageSplit:
            word = word.lower()
            # Checks if the user wants a 10 pull
            if word == "10":
                commands.tenPull = 10
            elif word == "lc" or word == "lightcone":
                lightConeTrigger = True
            else:
                charName = word

        return (lightConeTrigger, charName)

    async def initBannerType(self, isLightConeBanner, charName):
        """
        Initializes the type of banner the user wants to pull on.

        Tries to see if a LC banner is applicable. Then Limited Banner char. If not, then use Standard Banner.
        (Seems like a very bad way to do this tho so try to change it)
        """
        try:
            if isLightConeBanner:
                return await self.initLimitedLCBanner(charName)
            else:
                return await self.initLimitedCharBanner(charName)
        except:
            return await self.initStandardBanner()
        
    async def poolDecider(self):
        """Decides which rarity pool it will use to pull on"""
        if commands.simcounter >= 90:
            commands.chosenList = random.choices(commands.fiveStarPity, weights=(50,50), k=1)
            commands.simcounter = 0
            commands.isFiveStarGuaranteed = True
        elif commands.fourPityCounter >= 10:
            commands.chosenList = random.choices(commands.fourStarPity, weights=(49.2,49.2,(commands.fiveStarPityRateUp+1.0)/2.0,(commands.fiveStarPityRateUp+1.0)/2.0), k=1)
            commands.fourPityCounter = 0
        else:
            commands.chosenList = random.choices(commands.normalPull, weights=(94.3,2.55,2.55,commands.fiveStarPityRateUp/2.0,commands.fiveStarPityRateUp/2.0), k=1)
    
    async def pityDecider(self, bannerType):
        """Decides if this pull has reached any pity threshhold"""
        if list(fourStarLightCones.items()) == commands.chosenList[0] or list(fourStarHeroes.items()) == commands.chosenList[0] or (not bannerType and commands.chosenList[0] == commands.fourStarRateUp):
            commands.rarity = "★★★★☆"
            commands.fourPityCounter = 0

        elif list(fiveStarHeroes.items()) == commands.chosenList[0] or list(fiveStarLightCones.items()) == commands.chosenList[0] or (bannerType != "Standard" and commands.chosenList[0] == commands.fiveStarRateUp):
            commands.rarity = "★★★★★"
            commands.simcounter = 0
            commands.fiveStarPityRateUp = 0.6
            commands.fiveStarsPulled += 1

    async def limitedBannerDecider(self, bannerType):
        """Adds the limited five star focus the pool if it is a limited banner"""
        if commands.rarity == "★★★★★" and bannerType != "Standard":
            commands.chosenList += [commands.fiveStarRateUp]
            if bannerType == "Light Cone":
                commands.chosenList = random.choices(commands.chosenList, weights=(25,75), k=1)
            else:
                commands.chosenList = random.choices(commands.chosenList, weights=(50,50), k=1)
                
        commands.chosenPull = random.choice(commands.chosenList[0])

    async def limitedFiveStarGuaranteedPityDecider(self):
        """Decides if the user is guaranteed the five star focus unit if they had lost the 50/50 before this one."""
        if commands.isFiveStarGuaranteed:
            commands.chosenPull = commands.fiveStarRateUp[0]
            commands.isFiveStarGuaranteed = False
        elif commands.chosenPull not in commands.fiveStarRateUp:
            commands.isFiveStarGuaranteed = True

    async def limitedFourStarGuaranteedPityDecider(self):
        """Decides if the user is guaranteed a four star focus unit if they had gotten a non-focus four star before this one."""
        if commands.chosenPull not in commands.fourStarRateUp and not commands.isFourStarGuaranteed:
            commands.isFourStarGuaranteed = True
            commands.fourPityCounter = 0
        # Will force to pick one of the focus units if needed
        elif commands.chosenPull not in commands.fourStarRateUp and commands.isFourStarGuaranteed:
            commands.chosenPull = random.choice([commands.fourStarRateUp[0]])
            commands.isFourStarGuaranteed = False
            commands.fourPityCounter = 0
        else:
            commands.isFourStarGuaranteed = False
            commands.fourPityCounter = 0

    async def checkRarityForColor(self, bannerType):
        """Assigns embed coloring depending on the rarity of the chosen pull"""
        if commands.rarity == "★★★★★":
            if bannerType != "Standard":
                await self.limitedFiveStarGuaranteedPityDecider()
            commands.rarityColor = 0xffcf4a
            commands.imageUrl = commands.chosenPull[1]
        elif commands.rarity == "★★★★☆":
            if bannerType != "Standard":
                await self.limitedFourStarGuaranteedPityDecider()
            if commands.rarityColor != 0xffcf4a:
                commands.rarityColor = 0xa252e3
        elif not (commands.rarityColor == 0xffcf4a or commands.rarityColor == 0xa252e3):
            commands.rarityColor = 0x5dd6f5
        
    async def setTenPullEmbed(self, embedSummon, user):
        embedSummon.add_field(name=user.name, value="==============")
        embedSummon.add_field(name="Your Pulls: ", value=f"Current Pity after all pulls: {commands.simcounter}\nTotal Pulls: {commands.totalPulls}\nTotal Amount in USD: ${format(commands.totalAmountofMoneyWasted, '.2f')}\nFive Stars Pulled: {commands.fiveStarsPulled}", inline="False")
        embedSummon.set_image(url=commands.imageUrl)
        for x in range(len(commands.chosenTenPull)):
            embedSummon.add_field(name=commands.chosenTenPull[x][0][0].upper() + commands.chosenTenPull[x][0][1:], value=commands.chosenTenRarity[x], inline="True")

    async def setSinglePullEmbed(self, embedSummon, user):
        embedSummon.add_field(name="User:", value=user.name)
        embedSummon.add_field(name="You have pulled: ", value=f"{commands.rarity}\n{commands.chosenPull[0][0].upper() + commands.chosenPull[0][1:]}")
        embedSummon.add_field(name="Current Pity Counter: ", value=commands.simcounter)
        embedSummon.add_field(name="Total Pulls: ", value=commands.totalPulls)
        embedSummon.add_field(name="Total Amount in USD: ", value=f"${format(commands.totalAmountofMoneyWasted, '.2f')}")
        embedSummon.add_field(name="Five Stars Pulled: ", value=commands.fiveStarsPulled)
        embedSummon.set_image(url=commands.chosenPull[1])

    # Helper Functions for StarRailUsers

    async def findUser(self, authorId):
        for i, x in enumerate(commands.userList):
            if x.name == authorId:
                return commands.userList[i]      
        return "None"

    async def createUser(self, authorId):
        user = starRailUsers(authorId)
        commands.userList.append(user)

        return user

    async def initUser(self, authorId):
        '''Initializes the user's stats for the summoning simulator. If the user is not found, it will create a new user.'''
        user = await self.findUser(authorId)
        if user == "None":
            return await self.createUser(authorId)
        
        await user.setStatsToSummon()
        return user

class starRailUsers():
    """#### Class that holds the user's stats for the summoning simulator."""
    def __init__(self, authorId):
        self.name = authorId

        self.fourPityCounter = 0
        self.fiveStarPityRateUp = 0.6
        self.simcounter = 0
        self.totalPulls = 0
        self.totalAmountofMoneyWasted = 0
        self.isFiveStarGuaranteed = False
        self.isFourStarGuaranteed = False
        self.fiveStarsPulled = 0

    async def setStatsToSummon(self):
        commands.fourPityCounter = self.fourPityCounter
        commands.fiveStarPityRateUp = self.fiveStarPityRateUp
        commands.simcounter = self.simcounter
        commands.totalPulls = self.totalPulls
        commands.totalAmountofMoneyWasted = self.totalAmountofMoneyWasted
        commands.isFiveStarGuaranteed = self.isFiveStarGuaranteed
        commands.isFourStarGuaranteed = self.isFourStarGuaranteed
        commands.fiveStarsPulled = self.fiveStarsPulled

    async def setSummonResultsToStats(self):
        self.fourPityCounter = commands.fourPityCounter
        self.fiveStarPityRateUp = commands.fiveStarPityRateUp
        self.simcounter = commands.simcounter
        self.totalPulls = commands.totalPulls
        self.totalAmountofMoneyWasted = commands.totalAmountofMoneyWasted
        self.isFiveStarGuaranteed = commands.isFiveStarGuaranteed
        self.isFourStarGuaranteed = commands.isFourStarGuaranteed
        self.fiveStarsPulled = commands.fiveStarsPulled

    async def clearPityFromAccount(self):
        self.fourPityCounter = 0
        self.fiveStarPityRateUp = 0.6
        self.simcounter = 0
        self.totalPulls = 0
        self.totalAmountofMoneyWasted = 0
        self.isFiveStarGuaranteed = False
        self.isFourStarGuaranteed = False
        self.fiveStarsPulled = 0

#Cog stuff from src that does stuff so I can make stuff so I can do stuff
def setup(client):
    client.add_cog(starrail(client))