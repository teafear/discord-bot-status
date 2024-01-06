import discord
from discord.ext import commands
from tokens import tokenortoken
from main import statusbotmain

client = commands.Bot(command_prefix='BOT')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.Online, activity=discord.game(statusbotmain))
    print('Бот включен!')

client.run(tokenortoken)