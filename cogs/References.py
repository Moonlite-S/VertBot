import discord
import asyncio
from discord.ext import commands

#If you ever want to start using cogs, here's a template
class myCog:
    def __init__(self, bot):
        self.bot = bot

#Cog stuff from src that does stuff so I can use stuff
def setup(bot):
    bot.add_cog(Reference(bot))
