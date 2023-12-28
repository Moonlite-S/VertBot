import discord
import random
from discord.ext import commands
from cogs.database.starrailData import *

class starrail(commands.Cog):
    ## TODO:
    #   * Create a summon sim
    #   * Implement the Soft Pity into the rates (Around 75 pulls, chances rises by 6% each pull)
    #   * Have it so that pity it counted separately for everyone

    ## Refactoring Tips:
    # * Maybe separate Standard and Limited banners into their own functions

    commands.fourPityCounter = 0
    commands.simcounter = 0
    commands.fiveStarPityRateUp = 0.6
    commands.totalPulls = 0
    commands.totalAmountofMoneyWasted = 0

    commands.rarityColor = 0
    commands.tenPull = 1
    commands.fiveStarsPulled = 0

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

    @commands.command(name="starrailwarp", aliases=["warp"])
    async def SWSummonSim(self, ctx):
        versionControl = "1.4"

        await self.resetBanner()
        charName = ""

        messageSplit = ctx.message.content[7:].split()
        charName = await self.decodeMessage(messageSplit)
        bannerType = await self.initBannerType(charName[0], charName[1])

        for x in range(commands.tenPull):
            await self.performSummon(bannerType)

        # Embed time
        embedSummon = discord.Embed(title=commands.bannerName, color=commands.rarityColor)
        embedSummon.set_thumbnail(url=commands.bannerImage)

        if commands.tenPull == 10:
            await self.setTenPullEmbed(embedSummon)
        else:
            await self.setSinglePullEmbed(embedSummon)
        
        embedSummon.set_footer(text=versionControl)
        await ctx.message.channel.send(embed=embedSummon)

    # Clears Current Pity
    @commands.command(name="clearpity", aliases=["clearp"])
    async def ClearPity(self, ctx):
        commands.fourPityCounter = 0
        commands.simcounter = 0
        commands.totalPulls = 0
        commands.fiveStarsPulled = 0
        commands.totalAmountofMoneyWasted = 0
        embedClear = discord.Embed(title="Pity has been cleared!", color=0x00ff00)
        await ctx.message.channel.send(embed=embedClear)

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
        print("Character not found. Assuming Standard Warp")
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

    async def decodeMessage(ctx, messageSplit):
        """
        ### Decodes the input from user to decide how the simulation will go
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
        """Initializes what type of banner it is. (Supports only Standard, Limited Character, and Light Cone Banners)"""
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
        "Assigns embed coloring depending on the rarity of the chosen pull"
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
        
    async def setTenPullEmbed(self, embedSummon):
        embedSummon.add_field(name="Your Pulls: ", value=f"Current Pity after all pulls: {commands.simcounter}\nTotal Pulls: {commands.totalPulls}\nTotal Amount in USD: ${format(commands.totalAmountofMoneyWasted, '.2f')}\nFive Stars Pulled: {commands.fiveStarsPulled}", inline="False")
        embedSummon.set_image(url=commands.imageUrl)
        for x in range(len(commands.chosenTenPull)):
            embedSummon.add_field(name=commands.chosenTenPull[x][0][0].upper() + commands.chosenTenPull[x][0][1:], value=commands.chosenTenRarity[x], inline="True")

    async def setSinglePullEmbed(self, embedSummon):
        embedSummon.add_field(name="You have pulled: ", value=f"{commands.rarity}\n{commands.chosenPull[0][0].upper() + commands.chosenPull[0][1:]}")
        embedSummon.add_field(name="Current Pity Counter: ", value=commands.simcounter)
        embedSummon.add_field(name="Total Pulls: ", value=commands.totalPulls)
        embedSummon.add_field(name="Total Amount in USD: ", value=f"${format(commands.totalAmountofMoneyWasted, '.2f')}")
        embedSummon.add_field(name="Five Stars Pulled: ", value=commands.fiveStarsPulled)
        embedSummon.set_image(url=commands.chosenPull[1])

#Cog stuff from src that does stuff so I can make stuff so I can do stuff
async def setup(client):
    await client.add_cog(starrail(client))