import discord
from discord.ext import commands

#A place where I have my E7 characters maybe? idk
class e7(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    


def setup(bot):
    bot.add_cog(pics(bot))