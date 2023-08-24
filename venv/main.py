# imports
import random
from colorama import Fore

# lets user choose name for player
#chosses name
def name_select():
    playerinfo = open("/home/ben/coding/counter/venv/info/playerinfo", 'w')

    print('hello')
    name = input('Choose your name: ')
    last_name = input('Choose your last name: ')

    playerinfo.write(name + '\n')
    playerinfo.write(last_name + '\n')

    full = name + last_name
    return full


#chooses place of living(pos)
def country_select():
    playerinfo = open("/home/ben/coding/counter/venv/info/playerinfo", 'a')

    pos = input('Choose where you live')
    playerinfo.write(pos + '\n')
    return pos


# sets the players age
# defult age starts at zero
def set_age():
    playerinfo = open("/home/ben/coding/counter/venv/info/playerinfo", 'a')

    age = '0'
    playerinfo.write(age + '\n')
    return age




# main command for loop
command = ''

# Commands list
commands = """
commands -- shows list of commands
whoami -- solves your existential crisis
> -- moves age up by one
exit -- pauses the simulation
killme -- deletes your character
actions -- shows list of availible actions
"""

actions = """
Dumb shit -- just be an idiot
Crime -- commit a crime
Job -- get a job
Love -- fine someone
School -- get your dumbass an education
"""

# Gives player the option to restart
print(Fore.RED + '!!WARNING: THIS WILL DELTE YOUR CURRENT CHARACTER')
psc = input(Fore.YELLOW + "Would you like to make a new character? Y/N ")


if psc == "Y" or psc == 'y' or psc == 'YES' or psc == 'yes':
    print(f"welcome to the world {name_select()} of {country_select()} your:{set_age()} years old!")
else:
    print('okay')

# Tells player main command
print("type 'commands' if you would like to see a list of commands")

# main
while command != 'exit':
    # opens playerinfo file
    info = open("/home/ben/coding/counter/venv/info/playerinfo", 'r')
    whoami = info.read()

    command = str(input(Fore.WHITE + '>>> '))
    if command == 'commands':
        print(Fore.BLUE + commands)
    elif command == '>':
        age = int(age) + 1
        print(f"You are now {age} years old.....")
    elif command == 'whoami':
        print(whoami)
    elif command == 'killme':
        yn = input('you sure')
        if yn == 'Y' or yn == 'y' or yn == 'yes' or yn == 'YES':
            print("Okay then....")
            info = open("/home/ben/coding/counter/venv/info/playerinfo", 'w')
            info.write('Nobody lmao')
        else:
            print('make up your mind')
    elif command == 'actions':
        print(Fore.BLUE + actions)
        action = input(Fore.WHITE + 'What would you like to do? ')
