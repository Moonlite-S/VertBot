from discord.ext import commands

class gptVert(commands.Cog):

    @commands.command(name="chat")
    async def chat(self, ctx):
        await ctx.send("Hello! I'm GPT-3. How can I help you today?")

#Cog stuff from src that does stuff so I can make stuff so I can do stuff
async def setup(client):
    await client.add_cog(gptVert(client))