import discord
import os
from discord.ext import commands
client = discord.Client

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():              # status=discord.Status.(Online,Idle,...)
    await client.change_presence(status=discord.Status.Online, activity=discord.ActivityType.watching(name='activity')) # name='название активности'
print('Мы вошли в систему как {0.user}'.format(client))


token_key = open('token.db', 'r')
token_key_content = token_key.read()
client.run(token_key_content)