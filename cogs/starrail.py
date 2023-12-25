from ast import alias
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

    @commands.command(name="starrailwarp", aliases=["warp"])
    # Warp Function (Standard, Limited, Departure)
    async def SWSummonSim(self, ctx):
        versionControl = "1.2"
        # Standard Warping
        normalPull = [list(threeStarLightCones.items()), list(fourStarHeroes.items()), list(fourStarLightCones.items()), list(fiveStarHeroes.items()), list(fiveStarLightCones.items())]
        fourStarPity = [list(fourStarHeroes.items()), list(fourStarLightCones.items()), list(fiveStarHeroes.items()), list(fiveStarLightCones.items())]
        fiveStarPity = [list(fiveStarHeroes.items()), list(fiveStarLightCones.items())]

        # Limited Warping
        fourStarRateUp = []
        fiveStarRateUp = []

        chosenTenPull = []
        chosenTenRarity = []
        rarityColor = 0

        tenPull = 1
        imageUrl = ""
        rarity = "★★★☆☆"

        bannerName = ""
        bannerImage = ""

        # Splits user input to check for key words
        messageSplit = ctx.message.content[7:].split()

        # Checks message for key words
        for word in messageSplit:
            # Checks if the user wants a 10 pull
            if word == "10":
                tenPull = 10
            else:
                # Alternate way (We need a function to call this. If the user wants the Light Cone banner or Char one)
                try:
                    fiveStarRateUp = [(word, limitedBanners[word]["Icon"])]
                    fourStarRateUp = limitedBanners[word]["Focus"]
                    bannerName = limitedBanners[word]["Name"]
                    bannerImage = limitedBanners[word]["BannerUrl"]
                    break
                except:
                    print("Character not found. (You aren't puttin spaces are ye?)")
                    return

        print(fiveStarRateUp + fourStarRateUp)

        for x in range(tenPull):
            rarity = "★★★☆☆"

            if (commands.simcounter >= 70):
                commands.fiveStarPityRateUp += 6

            commands.simcounter += 1
            commands.fourPityCounter += 1

            # Decides what pool to use
            if commands.simcounter >= 90:
                chosenList = random.choices(fiveStarPity, weights=(50,50), k=1)
                commands.simcounter = 1
            elif commands.fourPityCounter >= 10:
                chosenList = random.choices(fourStarPity, weights=(49.2,49.2,(commands.fiveStarPityRateUp+1.0)/2.0,(commands.fiveStarPityRateUp+1.0)/2.0), k=1)
                commands.fourPityCounter = 1
            else:
                chosenList = random.choices(normalPull, weights=(94.3,2.55,2.55,commands.fiveStarPityRateUp/2.0,commands.fiveStarPityRateUp/2.0), k=1)

            # Pity Detection
            if fourStarLightCones == chosenList[0] or fourStarHeroes == chosenList[0]:
                rarity = "★★★★☆"
                commands.fourPityCounter = 1
            elif fiveStarHeroes == chosenList[0] or fiveStarLightCones == chosenList[0]:
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
                rarityColor = 0xffcf4a
                imageUrl = chosenPull[1]
            elif rarity == "★★★★☆" and rarityColor != 0xffcf4a:
                rarityColor = 0xa252e3
            elif not (rarityColor == 0xffcf4a or rarityColor == 0xa252e3):
                rarityColor = 0x5dd6f5
            
            commands.totalPulls += 1

        embedSummon = discord.Embed(title="Stellar Warp", color=rarityColor)
        embedSummon.set_thumbnail(url="https://tinyurl.com/3cbmye89")

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

    @commands.command(name="clearpity", aliases=["cp", "clearp"])
    # Clears Current Pity
    async def ClearPity(self, ctx):
        commands.fourPityCounter = 0
        commands.simcounter = 0
        commands.totalPulls = 0


#Cog stuff from src that does stuff so I can make stuff so I can do stuff
async def setup(client):
    await client.add_cog(starrail(client))