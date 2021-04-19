import discord
import giphy_client
import os
import asyncio
import random
from discord.ext import commands, tasks
from giphy_client.rest import ApiException
from pprint import pprint

#Looks up Gifs in a jiffy, using Giphy's system and API
class gif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Looks up either a random or search gif
    @commands.command(name='gif', aliases=['GIF'])
    async def gif(self, ctx):
        user_input = ctx.message.content[6:]

        #Create an instance of the Giphy API
        api = giphy_client.DefaultApi()
        config = {
            'api_key' : os.getenv('GIPHY_TOKEN'),
            'limit' : 10,
            'rating' : 'm'
            }
        
        #If the user puts nothing, guide them how to use it
        if len(user_input) <= 1:
               emGif = discord.Embed(title="Gif Finder (by Giphy)", color=0x00ff00, description="Use --gif <keyword> to find a gif of something (certain keywords require all lower-case).")
               await ctx.message.channel.send(embed=emGif)

        #Some specific keywords
        elif user_input == "trending":
            try:
                api_response = api.gifs_trending_get(
                    config['api_key'], limit=config['limit'], rating=config['rating'])
                gif_lst = list(api_response.data)
                chosen_gif = random.choices(gif_lst)

                await ctx.message.channel.send(chosen_gif[0].url)

            except ApiException as e:
                await ctx.message.channel.send("Exception when calling DefaultApi->gifs_trending_get: %s\n" %e)
       
        elif user_input == "random":
            try:
                api_response = api.gifs_random_get(
                    config['api_key'], rating=config['rating'])
                gif_lst = list(api_response.data)
                chosen_gif = random.choices(lst)

                await ctx.message.channel.send(chosen_gif[0].url)

            except ApiException as e:
                await ctx.message.channel.send("Exception when calling DefaultApi->gifs_trending_get: %s\n" %e)
      
        elif user_input == "vert" or user_input == "Vert":
            vert = ["https://media1.tenor.com/images/cba644bd2b75eeb1d376a499f9043814/tenor.gif?itemid=20707383",
                    "https://media.tenor.com/images/2c633d38ddeb44af204df8bbfd8fb81a/tenor.gif",
                    "https://media1.tenor.com/images/863fd0d0beb6a02cbcf6ef5bccd8d2bd/tenor.gif?itemid=18641765", 
                    "https://media.tenor.com/images/a93987bdcfb9eac180a083f2bf79eef1/tenor.gif", 
                    "https://media.tenor.com/images/dc3cd81d1b7ce328f053649d4021ede2/tenor.gif",
                    "https://media.tenor.com/images/2628bd06af5c58c04b818eec90ece34c/tenor.gif",
                    "https://media.tenor.com/images/aed75ce079ed87f389f3c7513ae9153b/tenor.gif"
                ]

            await ctx.message.channel.send(random.choice(vert))
      
        #Custom keyword
        else:
            try:
                api_response = api.gifs_search_get(
                    config['api_key'], user_input, limit=config['limit'], rating=config['rating'])
                gif_lst = list(api_response.data)

                #If there are no searches, just leave
                if len(gif_lst) == 0:
                    gifEm = discord.Embed(title="There are no searches for that!", color=0x00ff00, description="Please try a differnt phrase.")
                    return await ctx.message.channel.send(embed=gifEm)

                else:
                    chosen_gif = random.choices(gif_lst)

                await ctx.message.channel.send(chosen_gif [0].url)

            except ApiException as e:
                return "Exception when calling DefaultApi->gifs_trending_get: %s\n" %e  

#Cog stuff from src that does stuff so I can use stuff
def setup(bot):
    bot.add_cog(gif(bot))