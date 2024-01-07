import os
from colorama import *
from setting import autostatus
if autostatus == False:
    print(Fore.GREEN+'Выберите статус для бота')
    print(Fore.WHITE+'1.'+Fore.YELLOW+ 'Играет(Playing)')
    print(Fore.WHITE+'2.'+Fore.YELLOW+ 'Смотрит(Watching)')
    print(Fore.WHITE+'3.'+Fore.YELLOW+ 'Слушает(Listening)')
    print(Fore.WHITE+'4.'+Fore.YELLOW+ 'Стримит(Streaming)'+Fore.WHITE)

    stats=input()
    if stats=='1':
        print(Fore.WHITE+"Вы выбрали статус" +Fore.YELLOW+ ' Играет(Plating)')
        status = 1
        status_act = open('status.db', 'w')
        status_act.write(status)
        status_act.close()
        os.system('play.py')

    if stats=='2':
        print(Fore.WHITE+"Вы выбрали статус" +Fore.YELLOW+ ' Смотрит(Watching)')
        status = 2
        status_act = open('status.db', 'w')
        status_act.write(status)
        status_act.close()
        os.system('watch.py')

    if stats=='3':
        print(Fore.WHITE+"Вы выбрали статус" +Fore.YELLOW+ ' Слушает(Listening)')
        status = 3
        status_act = open('status.db', 'w')
        status_act.write(status)
        status_act.close()
        os.system('list.py')
            
    if stats=='4':
        print(Fore.WHITE+"Вы выбрали статус" +Fore.YELLOW+ ' Стримит(Streaming)')
        status = 4
        status_act = open('status.db', 'w')
        status_act.write(status)
        status_act.close()
        os.system('stream.py')
else:
    status = open('status.db', 'r')
    status_content = status.read()
    if status_content == "1":
        os.system('play.py')
    elif status_content == "2":
        os.system('watch.py')
    elif status_content == "3":
        os.system('list.py')
    elif status_content == "4":
        os.system('stream.py')
    else: print('ОШИБКА! ПОСТАВЬТЕ ЗНАЧЕНИЕ false В autostatus В ФАЙЛЕ setting.py ')
