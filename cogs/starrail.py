from ast import alias
from click import command
import discord
import random
from discord.ext import commands, tasks
from cogs.database.starrailData import *

class starrail(commands.Cog):
    ## TODO:
    #   * Create a summon sim
    #   * Implement the Soft Pity into the rates (Around 75 pulls, chances rises by 6% each pull)
    #   * Have it so that pity it counted separately for everyone

    commands.fourPityCounter = 0
    commands.simcounter = 0
    commands.fiveStarPityRateUp = 0.6
    commands.totalPulls = 0
    commands.totalAmountofMoneyWasted = 0
    commands.isFiveStarGuaranteed = False
    commands.isFourStarGuaranteed = False

    # Standard Warping
    commands.normalPull = [list(threeStarLightCones.items()), list(fourStarHeroes.items()), list(fourStarLightCones.items()), list(fiveStarHeroes.items()), list(fiveStarLightCones.items())]
    commands.fourStarPity = [list(fourStarHeroes.items()), list(fourStarLightCones.items()), list(fiveStarHeroes.items()), list(fiveStarLightCones.items())]
    commands.fiveStarPity = [list(fiveStarHeroes.items()), list(fiveStarLightCones.items())]

    # Limited Warping
    commands.fourStarRateUp = []
    commands.fiveStarRateUp = []

    commands.bannerName = ""
    commands.bannerImage = ""
    
    @commands.command(name="starrailwarp", aliases=["warp"])
    # Warp Function (Standard, Limited, or Light Cones)
    async def SWSummonSim(self, ctx):
        versionControl = "1.3"

        chosenTenPull = []
        chosenTenRarity = []
        rarityColor = 0

        tenPull = 1
        imageUrl = ""
        rarity = "★★★☆☆"

        isLightConeBanner = False
        isStandardWarp = False

        # Splits user input to check for key words
        messageSplit = ctx.message.content[7:].split()

        # Checks message for key words
        for word in messageSplit:
            word = word.lower()
            # Checks if the user wants a 10 pull
            if word == "10":
                tenPull = 10
            elif word == "lc" or word == "lightcone":
                isLightConeBanner = True
            else:
                charName = word
                print(charName)

        # Initlizes what type of banner to do
        try:
            if isLightConeBanner:
                await self.initLCBanner(charName)
            else:
                await self.initCharBanner(charName)
        except:
            isStandardWarp = True
            commands.bannerName = "Stellar Warp"
            commands.bannerImage = "https://tinyurl.com/3cbmye89"
            print("Character (LC) not found. Assuming Standard Warp")

        for x in range(tenPull):
            rarity = "★★★☆☆"

            # Soft Pity increases chances of getting a 5-star by 6% linearly
            if (commands.simcounter >= 75):
                commands.fiveStarPityRateUp += 6

            commands.simcounter += 1
            commands.fourPityCounter += 1

            # Decides what pool to use
            if commands.simcounter >= 90:
                chosenList = random.choices(commands.fiveStarPity, weights=(50,50), k=1)
                commands.simcounter = 0
                commands.isFiveStarGuaranteed = True

            elif commands.fourPityCounter >= 10:
                chosenList = random.choices(commands.fourStarPity, weights=(49.2,49.2,(commands.fiveStarPityRateUp+1.0)/2.0,(commands.fiveStarPityRateUp+1.0)/2.0), k=1)
                commands.fourPityCounter = 0
            else:
                chosenList = random.choices(commands.normalPull, weights=(94.3,2.55,2.55,commands.fiveStarPityRateUp/2.0,commands.fiveStarPityRateUp/2.0), k=1)

            # Pity Reset Detection
            # (Only just checks if the lists are the same)
            if list(fourStarLightCones.items()) == chosenList[0] or list(fourStarHeroes.items()) == chosenList[0] or (not isStandardWarp and chosenList[0] == commands.fourStarRateUp):
                rarity = "★★★★☆"
                commands.fourPityCounter = 1
            elif list(fiveStarHeroes.items()) == chosenList[0] or list(fiveStarLightCones.items()) == chosenList[0] or (not isStandardWarp and chosenList[0] == commands.fiveStarRateUp):
                rarity = "★★★★★"
                commands.simcounter = 0
                commands.fiveStarPityRateUp = 0.6

            # Limited Banners are done 50/50, either getting the rate up unit or not
            # Limited Light Cone Banners follow the same thing but for 75/25, (75% chance to get rate up)
            if rarity == "★★★★★" and not isStandardWarp:
                chosenList += [commands.fiveStarRateUp]
                if isLightConeBanner:
                    chosenList = random.choices(chosenList, weights=(25,75), k=1)
                else:
                    chosenList = random.choices(chosenList, weights=(50,50), k=1)
                chosenPull = random.choice(chosenList[0])
            else:
                chosenPull = random.choice(chosenList[0])

            # Decides the color of the embed depending on rarity
            if rarity == "★★★★★":
                # Will forcefully change to focused 5 star if needed
                if not isStandardWarp and commands.isFiveStarGuaranteed:
                    chosenPull = commands.fiveStarRateUp[0]
                    commands.isFiveStarGuaranteed = False
                # If the user loses the 50/50 on limited banner
                elif not isStandardWarp and chosenPull not in commands.fiveStarRateUp:
                    commands.isFiveStarGuaranteed = True
                    
                rarityColor = 0xffcf4a
                imageUrl = chosenPull[1]

            elif rarity == "★★★★☆":
                # Checks to see if a four star is in the Focus pool
                if not isStandardWarp and chosenPull not in commands.fourStarRateUp and not commands.isFourStarGuaranteed:
                    commands.isFourStarGuaranteed = True
                    commands.fourPityCounter = 0
                # Will force to pick one of the focus units if needed
                elif not isStandardWarp and chosenPull not in commands.fourStarRateUp and commands.isFourStarGuaranteed:
                    chosenPull = random.choice([commands.fourStarRateUp[0]])
                    commands.isFourStarGuaranteed = False
                    commands.fourPityCounter = 0
                else:
                    commands.isFourStarGuaranteed = False
                    commands.fourPityCounter = 0
        
                if rarityColor != 0xffcf4a:
                    rarityColor = 0xa252e3
            elif not (rarityColor == 0xffcf4a or rarityColor == 0xa252e3):
                rarityColor = 0x5dd6f5
                        
            # Gather list of pulls if 10 pull
            if tenPull == 10:
                chosenTenPull += [chosenPull]
                chosenTenRarity += [rarity]

            commands.totalPulls += 1
            commands.totalAmountofMoneyWasted += 2.65

        embedSummon = discord.Embed(title=commands.bannerName, color=rarityColor)
        embedSummon.set_thumbnail(url=commands.bannerImage)

        if tenPull == 10:
            # Ten Summons
            embedSummon.add_field(name="Your Pulls: ", value=f"Current Pity after all pulls: {commands.simcounter}\nTotal Pulls: {commands.totalPulls}\n Total Amount in USD: ${format(commands.totalAmountofMoneyWasted, '.2f')}", inline="False")
            embedSummon.set_image(url=imageUrl)
            for x in range(len(chosenTenPull)):
                embedSummon.add_field(name=chosenTenPull[x][0][0].upper() + chosenTenPull[x][0][1:], value=chosenTenRarity[x], inline="True")
        else:
            # Single Summons
            embedSummon.add_field(name="You have pulled: ", value=f"{rarity}\n{chosenPull[0][0].upper() + chosenPull[0][1:]}")
            embedSummon.add_field(name="Current Pity Counter: ", value=commands.simcounter)
            embedSummon.add_field(name="Total Pulls: ", value=commands.totalPulls)
            embedSummon.add_field(name="Total Amount in USD: ", value=f"${format(commands.totalAmountofMoneyWasted, '.2f')}")
            embedSummon.set_image(url=chosenPull[1])
        
        embedSummon.set_footer(text=versionControl)
        await ctx.message.channel.send(embed=embedSummon)

    # Clears Current Pity
    @commands.command(name="clearpity", aliases=["clearp"])
    async def ClearPity(self, ctx):
        commands.fourPityCounter = 0
        commands.simcounter = 0
        commands.totalPulls = 0
        commands.totalAmountofMoneyWasted = 0
        embedClear = discord.Embed(title="Pity has been cleared!", color=0x00ff00)
        await ctx.message.channel.send(embed=embedClear)

    async def initCharBanner(self, word):
        commands.fiveStarRateUp = [(word, limitedBanners[word]["Icon"])]
        commands.fourStarRateUp = limitedBanners[word]["Focus"]
        commands.bannerName = limitedBanners[word]["Name"]
        commands.bannerImage = limitedBanners[word]["BannerUrl"]
        print("Character Time")

    async def initLCBanner(self, word):
        commands.fiveStarRateUp = [(limitedBanners[word]["LightConeName"], limitedBanners[word]["LightConeUrl"])]
        commands.fourStarRateUp = limitedBanners[word]["LightConeFocus"]
        commands.bannerName = limitedBanners[word]["LightConeName"]
        commands.bannerImage = limitedBanners[word]["LightConeThumbnailUrl"]
        print("Light Cone Time")

    async def resetBanner(self):
        # Reset Info
        commands.fourStarRateUp = []
        commands.fiveStarRateUp = []

        commands.bannerName = ""
        commands.bannerImage = ""
        print("Debug: reset rate ups")



#Cog stuff from src that does stuff so I can make stuff so I can do stuff
async def setup(client):
    await client.add_cog(starrail(client))