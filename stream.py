import discord
import os
from discord.ext import commands
from colorama import *


client = discord.Client

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event       
async def on_ready():                                       # name='название активности'
    await client.change_presence(activity=discord.Streaming(name='activity', url='https://www.twitch.tv/5eafear')) #url='Ссылка на стрим Twitch или YouTube'
print('Мы вошли в систему как {0.user}'.format(client))

token_key = open('token.db', 'r')
token_key_content = token_key.read()
client.run(token_key_content)