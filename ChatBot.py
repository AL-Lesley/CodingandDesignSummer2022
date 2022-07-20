#Intro
print('Hi! I\'m ChatBot')
name = input('What\'s your name?\n')#Stores users names
print('Hello, '+name+'!')
color = input('What\'s your favorite color?\n')#Stores users favorite color
print('hmmmm, '+color+'. Not my first choice...')
print('But, it\'s pretty cool\n')

#Temp Coversion
print('It\'s pretty hot where I am')
tempF= input('What\'s the temp in Fahrenheit where you are?\n') #Stores temp in F collected from user
tempC = (float(tempF)-32)/1.8
print('In Celcius that\'s '+str(round(tempC,2))+' degrees\n')
print('Oooo, I like showing off my math skills\n')
heightIn = input('What is your height in inches?\n')
heightMM = round(float(heightIn)*25.4,2)#convert inches to mm
print('You seem very tall if I say you are ' + str(heightMM)+'mm!\n')

#Music conversation
song= input('What is your favorite song?\n')
artist=input('Remind me... Who\'s song is that?\n')
print('Don\'t get me wrong... I love \'' + song + '\' but, ' + artist + '\'s earlier work was much better\n')

#Feelings Conversations
feeling = input('How have you been feeling today?\n')
feelingExplanation= input('What happened today to make you feel ' + feeling+'?\n')
print('Well then it makes sense you feel ' + feeling +'\n')

#Goodbye
print('I had a good chat ' +name+', but I think it\'s quitting time')
print('Maybe ' + color+' will grow on me!')
