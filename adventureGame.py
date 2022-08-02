#imports time module to add pauses to adventure
import time
#imports random module to generate pseudo-random numbers
import random
#Set days until aid 
days = 365
#Creates a dictionary of crew members and their job
crew={'Tom':'Medic','Sally':'Botanist','Gill':'Electrical Engineer','Neil':'Geologist','Mary':'Mechanical Engineer'}

countdown = 3
#Create 2 different random integers
rand1=random.randint(0,4)
rand2=random.randint(0,4)
end=False
while(rand1==rand2):
    rand1=random.randint(0,4)
    rand2=random.randint(0,4)
group=[]
#Intro
print(
'┏━━━┓━━━━━━━━━┏┓━━━━━━━━━━━━━┏┓━━━━━━━━━━━━━━━━━━┏━┓┏━┓┏━━━┓┏━━━┓┏━━━┓\n'+
'┗┓┏┓┃━━━━━━━━┏┛┗┓━━━━━━━━━━━┏┛┗┓━━━━━━━━━━━━━━━━━┃┃┗┛┃┃┃┏━┓┃┃┏━┓┃┃┏━┓┃\n'+
'━┃┃┃┃┏━━┓┏━━┓┗┓┏┛┏┓┏━┓━┏━━┓━┗┓┏┛┏┓┏━━┓┏━┓━┏━┓━━━━┃┏┓┏┓┃┃┃━┃┃┃┗━┛┃┃┗━━┓\n'+
'━┃┃┃┃┃┏┓┃┃━━┫━┃┃━┣┫┃┏┓┓┗━┓┃━━┃┃━┣┫┃┏┓┃┃┏┓┓┗━┛━━━━┃┃┃┃┃┃┃┗━┛┃┃┏┓┏┛┗━━┓┃\n'+
'┏┛┗┛┃┃┃━┫┣━━┃━┃┗┓┃┃┃┃┃┃┃┗┛┗┓━┃┗┓┃┃┃┗┛┃┃┃┃┃┏━┓━━━━┃┃┃┃┃┃┃┏━┓┃┃┃┃┗┓┃┗━┛┃\n'+
'┗━━━┛┗━━┛┗━━┛━┗━┛┗┛┗┛┗┛┗━━━┛━┗━┛┗┛┗━━┛┗┛┗┛┗━┛━━━━┗┛┗┛┗┛┗┛━┗┛┗┛┗━┛┗━━━┛\n'+
'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n'+
'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

time.sleep(1)
print('▒▄▀▄░░░▀▄▀▒██▀▒▄▀▄▒█▀▄░░░█▒█░█▄░█░▀█▀░█░█▒░░░▒▄▀▄░█░█▀▄\n░█▀█▒░░▒█▒░█▄▄░█▀█░█▀▄▒░░▀▄█░█▒▀█░▒█▒░█▒█▄▄▒░░█▀█░█▒█▄▀')
time.sleep(1)

print('You are one of the few choosen create a new civilization on mars')
time.sleep(1)
print('All martian civilians must survive as a team until this point\n')
time.sleep(1)
#Loop to display the names and professions of crew
print('You will be working with:')
for person in crew:
    print(person, 'who is the', crew[person])
    time.sleep(1)
#Choice 1: Personal item
print('\nYou are allowed 1 personal item')
choice1list=['Treasured Familiy Picture', 'Favorite Earth Snacks', 'A Good Book', 'A Utility Knife']
print('(1) Treasured Family Picture \n(2) Favorite Earth Snacks \n(3) A Good Book \n(4) Utility Knife\n')
choice1 = input('What will you bring?\n')
#If the choice is valid then 
try:
    choice1 = int(choice1)
    personalItem=choice1list[choice1-1]
    print('Hmmmm,',personalItem+', we\'ll see if that is a good choice\n') 
except:
    choice1 = '0'
    choice1=int(choice1)
    for i in range(5):
        print('.')
        time.sleep(.5)
    print('That\'s not a choice\n')
    print('You will bring nothing\n')
#Displays countdown from 3 to 1
while(countdown > 0):
    time.sleep(1)
    print(countdown,'\n')
    countdown-=1
#ASCII Art of rocketship 
print('  /\  \n  ||  \n  ||  \n  ||  \n/:||:\\\n|:||:|\n|/||\|\n  **  \n  **  ')
print('BlAST OFF!')
#Show a quick countdown of days from 365-344
for i in range(21):
    print('DAYS UNTIL AID:',days)
    days-=1
    time.sleep(.1)
#ASCII Art day 344
print(
'━━┏┓━━━━━━━━━━━━━━┏━━━┓┏┓━┏┓┏┓━┏┓\n'+
'━━┃┃━━━━━━━━━━━━━━┃┏━┓┃┃┃━┃┃┃┃━┃┃\n'+
'┏━┛┃┏━━┓━┏┓━┏┓━━━━┗┛┏┛┃┃┗━┛┃┃┗━┛┃\n'+
'┃┏┓┃┗━┓┃━┃┃━┃┃━━━━┏┓┗┓┃┗━━┓┃┗━━┓┃\n'+
'┃┗┛┃┃┗┛┗┓┃┗━┛┃━━━━┃┗━┛┃━━━┃┃━━━┃┃\n'+
'┗━━┛┗━━━┛┗━┓┏┛━━━━┗━━━┛━━━┗┛━━━┗┛\n'+
'━━━━━━━━━┏━┛┃━━━━━━━━━━━━━━━━━━━━\n'+
'━━━━━━━━━┗━━┛━━━━━━━━━━━━━━━━━━━━\n')
#Choice 2: Volunteer to Find Source of Alarm 
print('The whole cabin is awoken to beeping and flashing red lights')
check = input('Do you want to venture to check out what is wrong?\n')
#If the user chooses yes they will be able to choose a partner from the crew
if(check =='yes' or check=='Yes'):
    time.sleep(.5)
    print('\nYou may choose a partner to bring with you\n')
    for person in crew:
        print(person ,'who is the', crew[person])
        time.sleep(1)
    time.sleep(.5)
    #Choice 2-a: Partner
    partner=input('\nWho will you bring?\n')
    #Adds user and partner to the list 'group'
    group.append('you')
    group.append(partner)
else:
    #if user does not volunteer 2 random crew members are selected
    print('You do not volunteer')
    time.sleep(.5)
    print('Crew decide to pull straws to decide 2 crew members')
    time.sleep(.5)
    i=0
    #Add selected crew to search group
    for person in crew:
        if(i==rand1 or i==rand2):
            group.append(person)
        i+=1
    print(group[0],'and',group[1],'were chosen')
partner=''
#If gill the electrical engineer is in the group the group finds the source
if('Gill' in group or 'gill' in group):
    if(group[0]=='Gill'):
        partner=group[1]
    else:
        partner=group[0]
    print('Gill convinces', partner,'to check to main control panel')
    time.sleep(.5)
    print('The team looks at the monitor...\n')
    time.sleep(.5)
    print('THE SHIP IS OFF COURSE AND ABOUT TO COLLIDE WITH AN UNKNOWN PLANET\n')
    time.sleep(2)
    print('Gill knows how to fix the problem, but she cannot open the mainboard enclosure')
    #If the user's choice1 was the knife then the group is safe!
    if(personalItem=='A Utility Knife'):
        print('\nYou offer your knife')
        time.sleep(2)
        print('\nGILL IS ABLE TO REPAIR AND RIGHT THE SHIP\'S PATH!')
        time.sleep(2)
        end=True
    else:
        #If the user did not choose knife the mission fails
        print('\nYou do not have anything to help open the enclosure\n')
        time.sleep(2)
        print('Gill fails to right the ship\'s path\n')
        time.sleep(2)
#if mary the mechanical engineer is in the group, but not Gill the group goes to the engine room
elif('Mary' in group or 'mary' in group):
    if(group[0]=='Mary'):
        partner=group[1]
    else:
        partner=group[0]
    print('Mary convinces', partner,'to check to main engine')
        
else:
    #if neither mary nor gill are in the group wanders
    print(group[0], 'and', group[1], 'waste 15 minutes attempting to locate the source of the problem')
    time.sleep(.5)
if(end==False):
    time.sleep(1)
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n'+
'░     ░░░░░░░░░░░  ░░░░░░░░    ░░░░░   ░░░░     ░░░░\n'+
'▒  ▒▒   ▒▒▒▒▒▒▒▒  ▒  ▒▒▒▒▒▒  ▒   ▒▒▒   ▒▒  ▒▒▒▒   ▒▒\n'+
'▒  ▒▒▒   ▒▒▒▒▒▒  ▒▒   ▒▒▒▒▒   ▒   ▒▒   ▒  ▒▒▒▒▒▒▒▒▒▒\n'+
'▓      ▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓▓   ▓▓   ▓   ▓   ▓▓▓▓▓▓▓▓▓\n'+
'▓  ▓▓▓▓   ▓▓▓       ▓   ▓▓▓   ▓▓▓  ▓   ▓   ▓▓▓      \n'+
'▓  ▓▓▓▓▓  ▓▓   ▓▓▓▓▓▓▓   ▓▓   ▓▓▓▓  ▓  ▓▓   ▓▓▓▓  ▓▓\n'+
'█    █   ██   █████████   █   ██████   ███      ████\n'+
'████████████████████████████████████████████████████\n')
    time.sleep(.5)
    #if user is in a group with mary they are expelled from the ship in the crash
    if('you'in group and 'Mary' in group):
        print('You and Mary were shot into space while searching in the engine room')
    else:
        
        print('You are thrown across the spaceship and are knocked unconscious\n')
        time.sleep(.5)
        print('You look out the window and see an ecosystem unknown to you\n')
        time.sleep(.5)
        print('You search the cabin for your crewmates')
        #All crew in the engine room are lost
        if('Mary' in group):
            lost3=crew.pop('Mary')
            lost4=crew.pop(partner)
        #2 random crew members are removed
        lost1= crew.popitem()
        lost2= crew.popitem()
        time.sleep(.5)
        #display remaining crew
        print('You find:')
        for person in crew:
            print(person)
            time.sleep(.5)
        print('\nNone of the crew have found the remaining members\n')
        time.sleep(.5)
        print(
    '           .-\"\"\"\"-.       .-\"\"\"\"-.          \n'+
    '          /        \     /        \         \n'+
    '         /_        _\   /_        _\        \n'+
    '        // \      / \\ // \      / \\       \n'+
    '        |\__\    /__/| |\__\    /__/|       \n'+
    '         \    ||    /   \    ||    /        \n'+
    '          \        /     \        /         \n'+
    '           \  __  /       \  __  /          \n'+
    '   .-\"\"\"\"-. \'.__.\'.-\"\"\"\"-. \'.__.\'.-\"\"\"\"-.   \n'+
    '  /        \ |  |/        \ |  |/        \  \n'+
    ' /_        _\|  /_        _\|  /_        _\ \n'+
    '// \      / \\ // \      / \\ // \      / \\\n'+
    '|\__\    /__/| |\__\    /__/| |\__\    /__/|\n'+
    ' \    ||    /   \    ||    /   \    ||    / \n'+
    '  \        /     \        /     \        /  \n'+
    '   \  __  /       \  __  /       \  __  /   \n'+
    '    \'.__.\'         \'.__.\'         \'.__.\'    \n'+
    '     |  |           |  |           |  |     \n'+
    '     |  |           |  |           |  |     \n')
        #Choice 3: Alien Encounter
        alienChoice= input('(1)Offer aliens '+personalItem+' (2) Offer crew member\n')
        #if personal item is snacks crew is saved
        if alienChoice=='1' and personalItem=='Favorite Earth Snacks':
            print('The aliens accept your offer and help to fix your ship!')
        elif alienChoice=='1':
            print('They did not like your item')
            time.sleep(.5)
            print('The aliens did not show kindness to the crew')
        else:
            print('The aliens were offended you did not show loyalty to your crew')
            time.sleep(.5)

            print('The aliens did not show you kindness')
