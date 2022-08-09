#Imports time and random modules for pauses and picking random ints and elements
import random
import time

#Get the number of turns for each player and the number of dice
#that will be rolled each turn from the player
numDice = input('Choose Number of Dice(1-10): ')

while((not(numDice.isdigit()))or( numDice.isdigit() and (int(numDice)<1 or int(numDice)>10))):
    numDice = input('Choose Number of Dice(1-10): ')
numDice=int(numDice)
numTurns= input('Choose Number of Turns for Each Player(2-5): ')
while((not(numTurns.isdigit()))or( numTurns.isdigit() and (int(numTurns)<2 or int(numTurns)>5))):
    numTurns= input('Choose Number of Turns for Each Player(2-5): ')
numTurns=int(numTurns)
#Defines function that populates a list with random integers values 1-6
#Parameter determines length of list
def roll(num):
    results =[]
    for i in range(num):
        results.append(random.randint(1,6))
    #function returns the populated list
    return results
#Define function that takes in a list of numbers that represent
#the results of dice that were rolled for a player turn and a list
#of choices the user made to (r)reroll of (-)hold
#Returns the modified list of dice results
def reroll(choices,dice_list):
    print('ROLLING')
    for i in range(3):
        time.sleep(.5)
        print('.')
    #Loops through the list of player choices
    #If the element is 'r' then a new num 1-6 is picked    
    for i in range(len(choices)):
        if(choices[i]=='r'):
            dice_list[i]=random.randint(1,6)
    return dice_list
#Defines a function for the computer's strategy
#Parameters: A list of the results of the computer's first dice roll,
#num of dice rolled per turn
def compStrat(compRolls,numDice):
    print('Computer is Thinking')
    for i in range(3):
        time.sleep(.5)
        print('.')
    compChoices = ''
    for i in range(numDice):
        if compRolls[i]<5:
            compChoices = compChoices+('r')
        else:
            compChoices = compChoices + ('-')
    return compChoices
#Defines function to find winner
#Parameters: finals lists of roll results of computer and user
def findWinner(userList,compList):
    #Sum lists
    compTotal = sum(compList)
    userTotal = sum(userList)
    if(userTotal>compTotal):
        print('You Win with',userTotal,'Points!')
    elif(compTotal>userTotal):
        print('Computer Wins with',compTotal,'Points')
    else:
        print('You and the Computer Tie with', compTotal,'Points')
#Defines Function to check if comp needs to reroll        
def rerollCheck(compR):
    rerollNeed=False
    l=0
    while(rerollNeed==False and l<numDice):
        l+=1
        if(compR[i]<5):
           return True

#Start Game
input('Press any key to begin')

#first roll
userRoll = roll(numDice)
compRoll = roll(numDice)
#loops for every turn -1st roll
for i in range(numTurns-1):
    time.sleep(1)
    print('\nROLL', i+1,'\n')
    print('Your Roll:', userRoll)
    #Ask user if they want to change any rolls
    skip=input('Skip turn(y/n)')
    while not(skip.lower()=='y' or skip.lower()=='n'):
        skip=input('Skip turn(y/n)')
    if skip.lower()=='n':
        print('For Each Die, Choose to Re-Roll or Hold')
        rerollChoices = input('(r) Reroll , (-) Hold\n')
        while(len(rerollChoices)<numDice):
            print('Enter values for all dice')
            rerollChoices = input('(r) Reroll , (h) Hold')
            rerollChoices= rerollChoices.lower()
        userRR = reroll(rerollChoices,userRoll)
        print('Your New Roll:', userRR)
    time.sleep(.5)
    print('Computer\'s Roll:', compRoll)
    time.sleep(.5)
    rerollNeeded= rerollCheck(compRoll)
    #Reroll if computer has any rolls under 5
    if rerollNeeded==True:
        compChoices = compStrat(compRoll,numDice)
        print('Computer Rerolls')
        compRR =reroll(compChoices,compRoll)
        time.sleep(1)
        print('Computer\'s New Roll:', compRR)

#Find and display game winner
findWinner(userRoll,compRoll)

