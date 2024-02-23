import discord
import asyncio
from discord.ext import commands, tasks

#Help desk
class helpVert(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Groups up subcommands for easier access and readibility
    @commands.group(name='helpV', aliases=['helpv','help'], pass_content=True, invoke_without_command=True)
    async def helpV(self, ctx):
        emHelp = discord.Embed(title="Help Section", color = 0x00ff00, description="Use --help or --helpV <command> for extended information about a command.")

        emHelp.add_field(name = "General Commands", value = "version, help")
        emHelp.add_field(name = "Games", value = "8ball, rps, animequiz, hangman")
        emHelp.add_field(name = "Star Rail", value = "warp, clearpity")
        emHelp.add_field(name = "Vert Chat", value = "chat")
        emHelp.add_field(name = "Misc.", value = "hello, reee")

        if ctx.invoked_subcommand is None:
            await ctx.channel.send(embed = emHelp)

    # General Commands
    @helpV.group(name="version", aliases=["Vert", "vert", "v"])
    async def version(self, ctx):
        await self.createEmbed("Verion", "Show the current version of VertBot.", "--version", ctx)

    @helpV.group(name="help")
    async def help(self, ctx):
        await self.createEmbed("Help", "Shows all the possible commands of VertBot", "--help", ctx)
    
    # Games
    @helpV.group(name="ball8", aliases=['8ball'])
    async def ball8(self, ctx):
        await self.createEmbed("8Ball", "Ask the 8ball a question!", "--8ball <question> ?", ctx)

    @helpV.group(name="rps")
    async def rps(self, ctx):
        await self.createEmbed("Rock, Paper, Scissors", "Play rock, paper, scissors with Vert.", "--rps <rock \|\| paper \|\| scissors>", ctx)

    @helpV.group(name="animequiz", aliases=['aq'])
    async def animequiz(self, ctx):
        await self.createEmbed("Anime Quizshow", "Test your anime knowledge by guessing the anime using the most confusing and out of context hints ever.", "--animequiz --aq", ctx)

    @helpV.group(name="hangman", aliases=['hm'])
    async def hangman(self, ctx):
        await self.createEmbed("Hangman Minigame", "Play hangman with Vert!", "--hangman --hm", ctx)

    # Star Rail
    @helpV.group(name="starrailwarp", aliases=['warp'])
    async def stellarWarp(self, ctx):
        await self.createEmbed("Honkai Star Rail Warp Simulator", "Simulate summoning on either the Limited or Stellar Warp!\n\nParameters:\nCharacter - Any limited character (without spaces!)\n10 - Type this in if you want to do a 10 pull\nlc - Type this in if you want to summon on the character's Light Cone Banner\n\nNote: Parameters can be done in any order so long as they have space in between. And the space is important.", "--warp [character] [10] [lc]", ctx)

    @helpV.group(name="clearpity", aliases=['clearp'])
    async def stellarWarp(self, ctx):
        await self.createEmbed("Honkai Star Rail Warp Simulator", "Clears pity from the current user.\n\n--clearpity or --clearp", ctx)

    # Misc
    @helpV.group(name="hello")
    async def hello(self, ctx):
        await self.createEmbed("Hello", "Say hi to Vert.", "--hello", ctx)

    @helpV.group(name="reee", aliases=['ree','reeee'])
    async def reee(self, ctx):
        await self.createEmbed("Reee","Vert reee's", "--reee", ctx)

    # Gpt Vert
    @helpV.group(name="chat", aliases=['gptchat'])
    async def chat(self, ctx):
        await self.createEmbed("chat","Have a conversation with Vert using ChatGPT.", "--chat <message>", ctx)

    #   Helper Function for the Embed   #
    async def createEmbed(self, title, desc, value, ctx):
        emHelp = discord.Embed(title=title, description=desc, color=0x00ff00)
        emHelp.add_field(name="**Syntax:**", value=value)
        await ctx.channel.send(embed=emHelp)


#Cog stuff from src that does stuff so I can use stuff
async def setup(bot):
    await bot.add_cog(helpVert(bot))