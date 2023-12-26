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
    #   * Make it so that the highest rarity unit is shown at the end of a ten pull

    commands.fourPityCounter = 0
    commands.simcounter = 0
    commands.fiveStarPityRateUp = 0.6
    commands.totalPulls = 0
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
        versionControl = "1.2"

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

        if isLightConeBanner:
            try:
                await self.initLCBanner(charName)
            except:
                isStandardWarp = True
                commands.bannerName = "Stellar Warp"
                commands.bannerImage = "https://tinyurl.com/3cbmye89"
                print("Character (LC) not found. Assuming Standard Warp")
        else:
            try:
                await self.initCharBanner(charName)
            except:
                isStandardWarp = True
                commands.bannerName = "Stellar Warp"
                commands.bannerImage = "https://tinyurl.com/3cbmye89"
                print("Character not found. Assuming Standard Warp")

        for x in range(tenPull):
            rarity = "★★★☆☆"

            # Soft Pity increases chances of getting a 5-star by 6% linearly
            if (commands.simcounter >= 75):
                commands.fiveStarPityRateUp += 6

            commands.simcounter += 1
            commands.fourPityCounter += 1

            # Decides what pool to use
            if commands.simcounter >= 90 and commands.isFiveStarGuaranteed and isStandardWarp == False:
                commands.simcounter = 0
                commands.isFiveStarGuaranteed = False
                rarity = "★★★★★"
                print("This was guaranteed 5 star!")

            elif commands.simcounter >= 90:
                chosenList = random.choices(commands.fiveStarPity, weights=(50,50), k=1)
                commands.simcounter = 0
                commands.isFiveStarGuaranteed = True
                print("Lost 50/50")

            elif commands.fourPityCounter >= 10 and commands.isFourStarGuaranteed and isStandardWarp == False:
                chosenList = [commands.fourStarRateUp]
                commands.fourPityCounter = 0
                commands.isFourStarGuaranteed = False
                rarity = "★★★★☆"
                print("This was guaranteed 4 star!")

            elif commands.fourPityCounter >= 10:
                chosenList = random.choices(commands.fourStarPity, weights=(49.2,49.2,(commands.fiveStarPityRateUp+1.0)/2.0,(commands.fiveStarPityRateUp+1.0)/2.0), k=1)
                commands.fourPityCounter = 0
                commands.isFourStarGuaranteed = True
                print("Lost 4 Star Focus!")
            else:
                chosenList = random.choices(commands.normalPull, weights=(94.3,2.55,2.55,commands.fiveStarPityRateUp/2.0,commands.fiveStarPityRateUp/2.0), k=1)

            # Pity Reset Detection
            # (Only just checks if the lists are the same)
            if list(fourStarLightCones.items()) == chosenList[0] or list(fourStarHeroes.items()) == chosenList[0]:
                rarity = "★★★★☆"
                commands.fourPityCounter = 1
            elif list(fiveStarHeroes.items()) == chosenList[0] or list(fiveStarLightCones.items()) == chosenList[0]:
                rarity = "★★★★★"
                commands.simcounter = 0
                commands.fiveStarPityRateUp = 0.6
            
            chosenPull = random.choice(chosenList[0])
            
            # Gather list of pulls if 10 pull
            if tenPull == 10:
                chosenTenPull += [chosenPull]
                chosenTenRarity += [rarity]

            # Decides the color of the embed depending on rarity
            if rarity == "★★★★★":
                # Will forcefully change to focused 5 star if needed
                if not isStandardWarp and commands.isFiveStarGuaranteed:
                    chosenPull = commands.fiveStarRateUp[0]
                    commands.isFiveStarGuaranteed = False
                    print("This one was pity")
                # If the user loses the 50/50 on limited banner
                elif not isStandardWarp and chosenPull not in commands.fiveStarRateUp:
                    commands.isFiveStarGuaranteed = True
                    print("Lost 50/50 on limited banner")
                    
                rarityColor = 0xffcf4a
                imageUrl = chosenPull[1]

            elif rarity == "★★★★☆":
                # Checks to see if a four star is in the Focus pool
                if not isStandardWarp and chosenPull not in commands.fourStarRateUp and not commands.isFourStarGuaranteed:
                    commands.isFourStarGuaranteed = True
                    commands.fourPityCounter = 0
                    print("Lost four star focus")
                # Will force to pick one of the focus units if needed
                elif not isStandardWarp and chosenPull in commands.fourStarRateUp and commands.isFourStarGuaranteed:
                    chosenPull = random.choice(commands.fourStarRateUp[0])
                    commands.isFourStarGuaranteed = False
                    commands.fourPityCounter = 0
                    print("Won the four star pity")
                
                if rarityColor != 0xffcf4a:
                    rarityColor = 0xa252e3
            elif not (rarityColor == 0xffcf4a or rarityColor == 0xa252e3):
                rarityColor = 0x5dd6f5
            
            commands.totalPulls += 1

        embedSummon = discord.Embed(title=commands.bannerName, color=rarityColor)
        embedSummon.set_thumbnail(url=commands.bannerImage)

        if tenPull == 10:
            # Ten Summons
            embedSummon.add_field(name="Your Pulls: ", value=f"Current Pity after all pulls: {commands.simcounter}\nTotal Pulls: {commands.totalPulls}", inline="False")
            embedSummon.set_image(url=imageUrl)
            for x in range(len(chosenTenPull)):
                embedSummon.add_field(name=chosenTenPull[x][0], value=chosenTenRarity[x], inline="True")
        else:
            # Single Summons
            embedSummon.add_field(name="You have pulled: ", value=f"{rarity}\n{chosenPull[0]}")
            embedSummon.add_field(name="Current Pity Counter: ", value=commands.simcounter)
            embedSummon.add_field(name="Total Pulls: ", value=commands.totalPulls)
            embedSummon.set_image(url=chosenPull[1])
        
        embedSummon.set_footer(text=versionControl)
        rarity = 3
        await ctx.message.channel.send(embed=embedSummon)

    # Clears Current Pity
    @commands.command(name="clearpity", aliases=["clearp"])
    async def ClearPity(self, ctx):
        commands.fourPityCounter = 0
        commands.simcounter = 0
        commands.totalPulls = 0
        embedClear = discord.Embed(title="Pity has been cleared!", color=0x00ff00)
        await ctx.message.channel.send(embed=embedClear)

    async def initCharBanner(self, word):
        commands.fiveStarRateUp = [(word, limitedBanners[word]["Icon"])]
        commands.fourStarRateUp = limitedBanners[word]["Focus"]
        commands.bannerName = limitedBanners[word]["Name"]
        commands.bannerImage = limitedBanners[word]["BannerUrl"]
        print("Character Time")
        print(f"5 Star Rate Up: {commands.fiveStarRateUp} \n4 Star Rate Up: {commands.fourStarRateUp}")

    async def initLCBanner(self, word):
        commands.fiveStarRateUp = [(limitedBanners[word]["LightConeName"], limitedBanners[word]["LightConeUrl"])]
        commands.fourStarRateUp = limitedBanners[word]["LightConeFocus"]
        commands.bannerName = limitedBanners[word]["LightConeName"]
        commands.bannerImage = limitedBanners[word]["LightConeThumbnailUrl"]
        print("Light Cone Time")
        print(f"5 Star Rate Up: {commands.fiveStarRateUp} \n 4 Star Rate Up: {commands.fourStarRateUp}")

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