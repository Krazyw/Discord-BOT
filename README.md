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

### How to setup (yeah)

- Download or Copy & Paste the code on your program (Python file, ofc)
- You'll need to download the libraries so open your command prompt or terminal and type this : 
`pip install discord.py`
- For every library in the code except for 'random' only if you don't want to include the 'dice' command in your bot


