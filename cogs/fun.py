from re import L
import discord
from discord.ext import commands
import aiohttp
import json

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        async with aiohttp.ClientSession() as session:
            data = await session.get("https://official-joke-api.appspot.com/jokes/random")
            data = await data.read()
            data = json.loads(data)
        embed = discord.Embed(title="Joke", color = discord.Color.green(), description=f"{data['setup']}\n||{data['punchline']}||")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as session:
            data = await session.get("https://meme-api.herokuapp.com/gimme/wholesomememes")
            data = await data.read()
            data = json.loads(data)
        embed= discord.Embed(title=data['title'].capitalize(), color = discord.Color.blue())
        embed.set_image(url=data['url'])
        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx):
        embed=discord.Embed()
        embed.set_image(url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def urban(self, ctx, *, word):
        async with aiohttp.ClientSession() as session:
            data = await session.get("http://urbanscraper.herokuapp.com/define/" + word.lower())
            data = await data.read()
            data = json.loads(data)
        try:
            embed = discord.Embed(title=f"Urban Search for : {data['term'].capitalize()}")
            embed.add_field(name="Definition", value=data['definition'].capitalize(), inline=False)
            embed.add_field(name="Example", value=data['example'].capitalize(), inline=False)
        except KeyError:
            await ctx.send(f"Term not found: **{word.capitalize()}**")
            return
        embed.set_footer(text=f"Requested by: {ctx.message.author}")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))
