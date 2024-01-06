import os
import time
from colorama import *
import sys
init()
statusbotmain = input(Fore.WHITE + "Напишите статус для бота " + Fore.YELLOW)

print(Fore.GREEN+'Выберите статус для бота')
print(Fore.WHITE+'1.'+Fore.YELLOW+ 'Играет(Playing)')
print(Fore.WHITE+'2.'+Fore.YELLOW+ 'Смотрит(Watching)')
print(Fore.WHITE+'3.'+Fore.YELLOW+ 'Слушает(Listening)')
print(Fore.WHITE+'4.'+Fore.YELLOW+ 'Стримит(Streaming)'+Fore.WHITE)

stats=input()
if stats=='1':
    print(Fore.WHITE+"Вы выбрали статус" +Fore.YELLOW+ ' Играет(Plating)')
    os.system('playing.py')

if stats=='2':
    print(Fore.WHITE+"Вы выбрали статус" +Fore.YELLOW+ ' Смотрит(Watching)')
    os.system('watching.py')

if stats=='3':
    print(Fore.WHITE+"Вы выбрали статус" +Fore.YELLOW+ ' Слушает(Listening)')
    os.system('listening.py')

if stats=='4':
    print(Fore.WHITE+"Вы выбрали статус" +Fore.YELLOW+ ' Стримит(Streaming)')
    os.system('streaming.py')
