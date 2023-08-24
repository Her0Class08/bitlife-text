import random

def name_select():
    playerinfo = open("/home/ben/coding/counter/venv/info/playerinfo", 'w')

    print('hello')
    name = input('choose your name')

    playerinfo.write(name)
    return f"Your name is: {name}"





print(name_select())