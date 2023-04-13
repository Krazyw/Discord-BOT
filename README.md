# Discord BOT
Here is a small bot discord in python that you can run on your computer or on machines (it is a very simple code nothing hard to understand)

### You'll have to download the libraries :

- import discord
- import requests
- import random
- from discord.ext import commands

### You can add commands with this :

```python
@bot.command()
async def example(ctx): # change the (example) to the name of the command you want
    await ctx.send('example') # basically send "example" when you type ",example"
```
- After the 'async def example(ctx):' line, you can add your code for what the Discord bot will do
