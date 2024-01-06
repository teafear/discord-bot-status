import discord
import os
import pylint
from tokens import tokenortoken
from discord.ext import commands
from main import statusbotmain
client = discord.Client

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord. Activity(type=discord.ActivityType.watching, name=statusbotmain))
print('Мы вошли в систему как {0.user}'.format(client))
token_key = tokenortoken
token_key_content = token_key.read()
client.run(token_key_content)