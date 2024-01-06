import discord
from discord.ext import commands
from token import token555

client = discord.Client

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord. Activity(type=discord.ActivityType.listening, name='Музыку'))
print('Мы вошли в систему как {0.user}'.format(client))

token_key = token555
token_key = token_key_content
token_key_content = token_key.read()
client.run(token_key_content)