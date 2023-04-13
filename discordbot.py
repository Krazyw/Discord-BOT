import discord
import requests
import random
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=';', intents=intents) # Change the ';' with the prefix you want to

@bot.event
async def on_ready():
    print('Bot Started')

@bot.command()
async def hello(ctx):
    await ctx.send('hello!')

# Only an example

@bot.command()
async def example(ctx): # change the (example) to the name of the command you want
    await ctx.send('example') # basically send "example" when you type ";example"

# Random dice number command

@bot.command()
async def dice(ctx, faces: int = 6, rolls: int = 1): # this basically do a random number command
    results = [random.randint(1, faces) for _ in range(rolls)]
    await ctx.send(f"The Results : {', '.join(str(r) for r in results)}")

bot.run('The token of your bot here!')
