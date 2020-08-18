import discord
from discord.ext import commands
from config import TOKEN
import os

bot = commands.Bot(command_prefix=">>")

@bot.event
async def on_ready():
    print("Ready")

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000, 2) # 364.98 ms
    await ctx.send(f"**Latency:** {latency} ms")

for i in os.listdir("./cogs"):
    if i.endswith(".py"):
        bot.load_extension(f"cogs.{i[:-3]}")

bot.run(TOKEN)