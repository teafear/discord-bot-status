import os
import time
from colorama import *

print('Небольшая настройка')

print('1.'+Fore.YELLOW+'autotoken'+Fore.WHITE+' - позволяет заходить без повторного ввода токена')
print('2.'+Fore.YELLOW+'autostatus'+Fore.WHITE+' - позволяет поставить статус без повторного выбора')
print('3.'+Fore.YELLOW+'autosetting'+Fore.WHITE+' - позволяет скипать настройку бота')
print('4.'+Fore.YELLOW+'autoupdate'+Fore.WHITE+' - позволяет отключить авто проверку обновления')
print('5.'+Fore.YELLOW+'update'+Fore.WHITE+' - проверяет наличие обновлений')
print('6.'+Fore.YELLOW+'autor'+Fore.WHITE+' - показывает информацию о создателе бота')
print(' ')
print(Fore.YELLOW+'skip'+Fore.WHITE+' - перейти дальше')

setting=input()
if setting=='1':
    print('Переходим в настройку autotoken')
    os.system('playing.py')

setting=input()
if setting=='2':
    print('Переходим в настройку autostatus')
    os.system('playing.py')

setting=input()
if setting=='3':
    print('Переходим в настройку autosetting')
    os.system('playing.py')

setting=input()
if setting=='4':
    print('Переходим в настройку autoupdate')
    os.system('playing.py')

setting=input()
if setting=='5':
    print('Проверяем наличие обновления')
    os.system('playing.py')

setting=input()
if setting=='6':
    os.system('main.py')




