import os
import time
from colorama import *
from setting import autotoken

if autotoken == True:
    init()
    token_1 = input( "Введите токен своего дискорд бота " + Fore.YELLOW)
    tokenortoken = token_1
    os.system('info.py')

else:
    print(Fore.YELLOW+'Autotoken'+Fore.WHITE+ ' выключен')
    os.system('info.py')


