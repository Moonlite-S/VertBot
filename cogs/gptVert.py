import discord
from openai import OpenAI
from discord.ext import commands


'''
TODO:
 - Format the output to be more readable
'''
class gptVert(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    commands.client = OpenAI()  
    
    # Vert's ongoing conversation with the user. Resets on bot restart
    commands.conversation = [{"role": "system", "content": "You are Vert from the popular video game franchise, Hyperdimension Neptunia. Vert is very kind with an elegant way of speaking. She likes helping people and sometimes references about her sister, Chika. Occasionally say 'Ara ara' at the end of your responses. You are also a fellow gamer that tends to use gamer lingo sometimes."}]

    @commands.command(name="chat")
    async def chat(self, ctx):
        '''
        #### Talk to Vert using ChatGPT-3.5!
        Usage: `--chat <message>`

        If no input is given, no response will be given.
        '''
        messageResponse = ctx.message.content[6:]

        if messageResponse == "":
            return
        
        # Limit the conversation list to 50 messages to avoid paying for more tokens
        # Since the conversation holds both user and bot's responses, it would only take around 25 commands before the list gets full
        if commands.conversation.len() > 50:
            del commands.conversation[:1]
        
        commands.conversation.append(await self.chatFormat("user", messageResponse))
        
        response = commands.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=commands.conversation,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        reply = response.choices[0].message.content

        commands.conversation.append(await self.chatFormat("assistant", reply))

        embed = discord.Embed(title="Vert", description=reply, color=0x00ff00)
        await ctx.channel.send(embed=embed)

    # Helper Functions #
    async def chatFormat(self, user, str):
        '''Formats the given str to be appended to the conversation list with the given user role.'''
        return {"role": user, "content": str}

#Cog stuff from src that does stuff so I can make stuff so I can do stuff
async def setup(client):
    await client.add_cog(gptVert(client))