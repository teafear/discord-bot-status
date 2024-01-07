
# 1.Тутор по установке
## Для начала скачаем Python ![Static Badge](https://img.shields.io/badge/python-black?style=flat&logo=python&link=https%3A%2F%2Fwww.python.org%2Fdownloads%2F)
## После его установки Python, запускаем командную строку и пишем следуйщие команды:

```py
pip install discord.py
```
```py
pip install discord
```
```py
pip install colorama
```
### Распаковываем файлы в любую папку

# 2.Тутор по настройке
## Запускаем файл start.py
Дальше следуем по инструкции.
Вводим Токен Бота > Выбераем статус боту
### Вопросы
## Как поменять статусы к примеру в watch.py ? 🟢🟡🔴
### Заходим в watch.py и обращаем внимание на элемент кода после @client.event
```py
async def on_ready():              # status=discord.Status.(меняем Online на Idle и...)
    await client.change_presence(status=discord.Status.Online, activity=discord.ActivityType.watching(name='activity')) # name='название активности'
```
## Как запускать бота без повторного ввода токена
### Если вы запусклиа бота и вы вводили токен своего бота, то ваш токен был автоматически добавлен в БД token.db
Вы можете включить функию в setting.py сменив значение False на True
```py
autotoken = True  #позволяет заходить без повторного ввода токена
```

## Как запускать бота без повторного выбора статуса
Вы можете включить функию в setting.py сменив значение False на True
```py
autostatus = False #позволяет поставить статус без повторного выбора
```
Обратите внимание, что будет запущен самый последний статус
# ТОЛЬКО ДЛЯ QPRO MOMENT

status.db содержит цифры от(1,2,3,4)
  1.Играет(Playing) 
  2.Смотрит(Watching) 
  3.Слушает(Listening)
  4.Стримит(Streaming)


  






