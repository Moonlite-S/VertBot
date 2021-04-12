import discord
import asyncio
from discord.ext import commands

#Help desk
class helpVert(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Groups up subcommands for easier access and readibility
    @commands.group(pass_content=True, invoke_without_command=True)
    async def helpV(self, ctx):
        em = discord.Embed(title="Help Section", color = 0x00ff00, description="Use --help <command> for extended information about a command.")

        em.add_field(name = "General Commands", value = "version, help")
        em.add_field(name = "Games", value = "8ball (use ball8 for more info), rps")
        em.add_field(name = "Misc.", value = "hello")

        if ctx.invoked_subcommand is None:
            await ctx.channel.send(embed = em)

    @helpV.group(name="version")
    async def version(self, ctx):
        em = discord.Embed(title = "Version", description = "Show the current version of VertBot.", color = 0x00ff00)
        em.add_field(name="**Syntax:**", value="--version")
        await ctx.channel.send(embed = em)

    @helpV.group(name="help")
    async def help(self, ctx):
        em = discord.Embed(title = "Help", description = "Shows all the possible commands of VertBot.", color = 0x00ff00)
        em.add_field(name="**Syntax:**", value="--help")
        await ctx.channel.send(embed = em)
    
    @helpV.group(name="ball8")
    async def ball8(self, ctx):
        em = discord.Embed(title = "8Ball", description = "Ask the 8ball a question.", color = 0x00ff00)
        em.add_field(name="**Syntax:**", value="--8ball <question> ?")
        await ctx.channel.send(embed = em)

    @helpV.group(name="rps")
    async def rps(self, ctx):
        em = discord.Embed(title = "Rock, Paper, Scissors", description = "Play rock, paper, scissors with Vert.", color = 0x00ff00)
        em.add_field(name="**Syntax:**", value="--rps <rock \|\| paper \|\| scissors>")
        await ctx.channel.send(embed = em)

    @helpV.group(name="hello")
    async def hello(self, ctx):
        em = discord.Embed(title = "Hello", description = "Say hi to Vert.", color = 0x00ff00)
        em.add_field(name="**Syntax:**", value="--hello")
        await ctx.channel.send(embed = em)


#Cog stuff from src that does stuff so I can use stuff
def setup(bot):
    bot.add_cog(helpVert(bot))