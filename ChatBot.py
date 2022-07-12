import time
import timeit
#start timer
start = timeit.default_timer()
#Intro
print('Hi! I\'m ChatBot')
name = input('What\'s your name?\n')
print('Hello, '+name+'!')
color = input('What\'s your favorite color?\n')

#Checks if the user color is blue or green 
if(color=='blue' or color=='Blue'):
    print('Yuck, I\'m more of a red person')
elif(color=='Red' or color=='red'):
    print('Good Taste!')
else:
    colorAnswer= input('Is '+color+' really a color?\n')
    if(colorAnswer=='yes'or colorAnswer=='Yes'or colorAnswer=='Y'or colorAnswer=='y'):
        print('Huh, good to know...')
        time.sleep(.5)
        print('I only know red and blue')
        time.sleep(1)
        print('At least it\'s not blue\n')
    else:
        colorAnswer2 =input('Do have a favorite color?\n')
        if 'no' in colorAnswer2 or 'No' in colorAnswer2 or 'don' in colorAnswer2:
            print('weird\n')
        else:
            print('So, you just won\'t tell me...')
            time.sleep(1)
            print('Feels a little rude')
time.sleep(.5)
feeling = input('How are you feeling today on a scale from 1-10?\n')
#Error handling for if user does not enter number
try:
    #converts string to int
    feeling= float(feeling)
    if(feeling>8 and feeling<11):
        print('Wow! Just from talking to me?\n')
    elif(feeling>6 and feeling <11):
        print('I\'d say that\'s pretty good\n')
    elif(feeling>4 and feeling <11):
        print('Could be worse!\n')
    elif(feeling>0 and feeling <11):
        print('Yikes\n')
    else:
        print('I said it had to be between 0 and 10!\n')
except:
    print('I just asked for a number  between 0 and 10.')
    time.sleep(.5)
    print('It\'s not that hard\n')
time.sleep(.5)
print('When I ask the questions, I don\'t seem so dumb!')
time.sleep(1)
print('Like I could almost pass the turing test!')
time.sleep(1)
askQuestion= input(name+', could you ask me a question?\n')
if(askQuestion=='no' or askQuestion=='No'):
    while(askQuestion!='yes'and askQuestion!='Yes'):
        askQuestion = input('please!\n')
        
if(askQuestion=='yes' or askQuestion=='Yes'):
    userQuestion=input('Sweet! Shoot\n')
    print('Ya, I have no idea how to answer that...')
    time.sleep(.5)
    print('I told you!')
    time.sleep(.5)
    print('I\'m not smart\n')
else:
    print('Ya, see I don\'t understand that at all')
time.sleep(1)

#stop timer    
stop = timeit.default_timer()

finalTime = stop-start
print('We have been chatting for', finalTime, 'seconds')
time.sleep(1)

print('That\'s', (finalTime)/60, 'Minutes')
time.sleep(1)

print('and', (finalTime)/360, 'Hours')
time.sleep(1)

print('That\'s too long!')
time.sleep(1)

print('Goodbye')

