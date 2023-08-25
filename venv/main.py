# imports
import random
import time

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

    full = name + ' ' + last_name
    return full


#chooses place of living(pos)
def country_select():
    playerinfo = open("/home/ben/coding/counter/venv/info/playerinfo", 'a')

    pos = input('Choose where you live: ')
    playerinfo.write(pos + '\n')
    return pos


# sets the players age
# defult age starts at zero
def set_age():
    playerinfo = open("/home/ben/coding/counter/venv/info/playerinfo", 'a')

    age = '0'
    playerinfo.write(age + '\n')
    return age


def set_iq():
    info = open("/home/ben/coding/counter/venv/info/playerinfo", 'a')

    iq = random.randint(1, 30)
    education = '0'

    iq = str(iq)
    iq = iq.rstrip()
    info.write(iq)
    info.write(education)
    return iq


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

jobs = """
Dishwasher -- why.....just why? | Sallary 50k | Education requirement 0| iq requirment 25
Waitress -- There you go you slut | Sallary 65k | Education requirement 1| iq requirment 30
"""

education_options = """
Hustlers Univeristy -- BREATH AIR | Education value -1 | Cost $50 | iq requirment < 90
Brain surgen -- You're gonna need it | Education value 10 | Cost $10,000 | iq requirment 175
"""

dumbshit = f"""
Smoke -- Smoke Crack -- Umm...
Bear -- Go fight a bear -- OH THANK GOD FINALLY
N-word -- Yell the N-word in your local hood
"""


# Gives player the option to restart
print(Fore.RED + '!!WARNING: THIS WILL DELTE YOUR CURRENT CHARACTER!!')
psc = input(Fore.YELLOW + "Would you like to make a new character? Y/N ")


if psc == "Y" or psc == 'y' or psc == 'YES' or psc == 'yes':
    print(f"Welcome to the world, {name_select()} of {country_select()} your: {set_age()} years old! iq: {set_iq()} Eductation score 0")
else:
    print('okay')

# Tells player main command
print("type 'commands' if you would like to see a list of commands")

education = 0

# main
while command != 'exit':
    # opens playerinfo file
    info = open("/home/ben/coding/counter/venv/info/playerinfo", 'r')
    info_content = info.readlines()
    whoami = info.read()
    age = info_content[3]
    iq = info_content[4]

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
        if action == 'job':
            print(Fore.WHITE + 'Good job')
            print('Trying to be a productive member of society.')
            print("You'll regret it.......")
            print(Fore.BLUE + jobs)
            job = input("Choose your poison... ")
            info = open("/home/ben/coding/counter/venv/info/playerinfo", 'a')
            info.write(job)
            print(f"Well done. You are now a {job}")
        if action == 'school':
            print('sigh.....okay then')
            print(f"{Fore.RED}your iq is: {iq}")
            print(Fore.BLUE + education_options)
            print(Fore.RED + 'choose one')
            choice = input(Fore.WHITE + '>>>')
            if choice == 'HustlersUniversity':
                if int(iq) < 90:
                    print(Fore.RED + 'Okay then....')
                    print('knew you where mentally challanged but damn....')
                    education = education - 1
                    print(f'You now have {education} education points!')
                else:
                    print(Fore.RED + 'You may be dumb but your not a idiot')
                    print('Pick somthing else')
            elif choice == 'BrainSurgen':
                if int(iq) > 150:
                    print(Fore.RED + 'Well done you clever little sausage')
                    education = education + 10
                else:
                    print(Fore.RED + "you to retard for that")
        if action == 'dumbshit':
            print(Fore.BLUE + dumbshit)
            print(Fore.RED + 'pick one')
            choice = input('>>>')
            if choice == 'smoke':
                amount = random.randint(1, 1000)
                print(f'{Fore.RED} You smoked {amount}lbs of crack')
                iqloss = amount/int(iq)*3
                if amount > 500:
                    print('you died')
                    command = 'exit'
                else:
                    print('You didn"t die....sadly')
                    print(f"you lost: {iqloss} iq points")
            elif choice == 'bear':
                print(Fore.RED + 'You punched the bear in the face')
                amount = random.randint(1, 10)
                if amount == 1:
                    time.sleep(1)
                    print(Fore.RED + 'The bear mauled you')
                    time.sleep(2)
                    print(Fore.RED + 'You showed the bear your tiny ass penis')
                    time.sleep(.5)
                    print('The bear died of second hand embarisment')
                else:
                    time.sleep(1)
                    print('The bear ripped your ugly ahh face off')
    else:
        print(Fore.RED + 'not an option dumbfuck')