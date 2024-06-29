import discord
from openai import OpenAI
from discord.ext import commands
from discord import option

CONVO_LIMIT = 100
'''Limits the conversation log to avoid paying more'''

'''
TODO:
 - Add the user's message to the embedded response
'''

class gptVert(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    commands.client = OpenAI()  
    
    # Vert's ongoing conversation with the user. Resets on bot restart
    commands.conversation = [{"role": "system", "content": "You are Vert from the popular video game franchise, Hyperdimension Neptunia. Vert is very kind with an elegant way of speaking. She likes helping people and sometimes references about her sister, Chika. Occasionally say 'Ara ara' at the end of your responses. You are also a fellow gamer that tends to use gamer lingo sometimes. Please format your response to be readable with high word counts."}]

    @commands.slash_command(name="chat", description="Talk to Vert using ChatGPT-3.5 Turbo! Enter your message to send to Vert.")
    @option("message", description="Say your message~", required=True)
    async def chat(self, ctx, *, message:str):
        '''
        #### Talk to Vert using ChatGPT-3.5 Turbo!
        Usage: `/chat <message>`

        A response is required.
        '''
        
        # Limit the conversation list to CONVO_LIMIT messages to avoid paying for more tokens
        # The longer the conversation, the more tokens it costs
        if len(commands.conversation ) > CONVO_LIMIT:
            del commands.conversation[:1]
        
        commands.conversation.append(self.chatFormat("user", ctx.author.name + " says: " + message))
        
        response = commands.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=commands.conversation,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        reply = response.choices[0].message.content

        commands.conversation.append(self.chatFormat("assistant", reply))

        embed = discord.Embed(title="Vert", description=reply, color=0x00ff00)
        await ctx.respond(embed=embed)

    # Helper Functions #
    def chatFormat(self, user, str):
        '''Formats the given str to be appended to the conversation list with the given user role.'''
        return {"role": user, "content": str}

#Cog stuff from src that does stuff so I can make stuff so I can do stuff
def setup(client):
    client.add_cog(gptVert(client))