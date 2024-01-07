import discord
import os
from discord.ext import commands
from colorama import *
from pathlib import Path
from setting import autotoken

if autotoken == False:
    init()
    token_1 = input( "Введите токен своего дискорд бота " + Fore.YELLOW)
    token_key = open('token.db', 'w')
    token_key.write(token_1)
    token_key.close()
    os.system('main.py')
else:
    os.system('main.py')