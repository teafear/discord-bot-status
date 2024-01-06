import os
import time
from colorama import *
from setting import autoinfo

if autoinfo == True:
    print('Небольшая настройка')
    print('Внимание все переменные находятся в setting.py')
    print(' ')
    print('1.'+Fore.YELLOW+'autotoken'+Fore.WHITE+' - позволяет заходить без повторного ввода токена')
    print('2.'+Fore.YELLOW+'autostatus'+Fore.WHITE+' - позволяет поставить статус без повторного выбора')
    print('3.'+Fore.YELLOW+'autoinfo'+Fore.WHITE+' - позволяет скипать инфо о настройке бота')
    print('4.'+Fore.YELLOW+'autoupdate'+Fore.WHITE+' - позволяет отключить авто проверку обновления')
    print(' ')
    print(Fore.YELLOW+'skip'+Fore.WHITE+' - перейти дальше')
    init()
    skipg = input( "Напишите skip " + Fore.YELLOW)
    if skipg == "skip":
        os.system('main.py')
    else:
        print(Fore.RED+ 'ОШИБКА! ПЕРЕЗАПУСКАЕМ info.py'+Fore.WHITE)
        os.system('info.py')
else:
    print(Fore.YELLOW+'Autoinfo'+Fore.WHITE+ ' выключен')
    os.system('main.py')


