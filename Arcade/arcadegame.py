from tkinter import *
import random
import time

cloudlist=[]
cloudnum=0
cloudspeed=1

window = Tk()
window.title('ICARUS')

#Create a canvas
canvas = Canvas(window, width=800, height=400, bg='blue')
canvas.pack()

#Create Sprite
img = PhotoImage(file='icarussprite.gif')
smallcloud=PhotoImage(file='smallcloud.gif')
largecloud=PhotoImage(file='largecloud.gif')

#Title screen
welcome_message = canvas.create_text(400,25, text = 'Icarus',fill='white',\
font =('times new roman', 30))
icarussprite = canvas.create_image(300,100,image=img)

#lives label
lives = 3
lives_display = Label(window, text='Lives :'+str(lives))
lives_display.pack()

#level label
level = 1
level_display = Label(window, text='Level :' + str(level))
level_display.pack()

# move chars and clouds
def move():
    canvas.move(icarussprite, 0, .5)
    for cloud in cloudlist:
        canvas.move(cloud, cloudspeed, 0)
    window.after(10,move)
    updatelevel()
    
#move based on key press
def moveoninput(keypress):
    key=keypress.keysym
    if key=='Left':
        canvas.move(icarussprite, -20,0)
    elif key=='Right':
        canvas.move(icarussprite, 20,0)
    elif key=='Up':
        canvas.move(icarussprite, 0,-20)
    elif key=='Down':
        canvas.move(icarussprite, 0,20)
        
# make cloud sprites
def makeclouds():
    global cloudnum
    size = random.randint(0,1)
    #pick a random y position
    yposition = random.randint(0, 400)
    if size==0:
        cloud = canvas.create_image(0,yposition,image=smallcloud)
    else:
        cloud = canvas.create_image(0,yposition,image=largecloud)
    cloudnum+=1
    cloudlist.append(cloud)
    window.after(2000,makeclouds)

#move cloud sprites
def moveclouds():
    for cloud in cloudlist:
        canvas.move(cloud, cloudspeed, 0)

# return if 2 items are touching
def collision(item1,item2,distance):
    overlap = False
    xdist = abs(canvas.coords(item1)[0] - canvas.coords(item2)[0])
    ydist = abs(canvas.coords(item1)[1] - canvas.coords(item2)[1])
    overlap = xdist<distance and ydist< distance
    return overlap

#clear clouds
def clearclouds():
    for cloud in cloudlist:
        cloud.destroy
        cloudlist.remove(cloud)
     
#update user lives
def updatelives():
    global lives
    lives -=1
    if lives == 0:
        gameover()
    lives_display.config(text='Lives: '+ str(lives))

#check if user hit cloud
def checkhits():
    for i in range(len(cloudlist)):
        if collision(icarussprite,cloudlist[i],80):
            updatelives()
    window.after(1000,checkhits)

#update level
def updatelevel():
    global level,cloudspeed,cloudnum
    if cloudnum > 10:
        cloudnum=0
        level+=1
        level_display.config(text='Level: '+ str(level))
        cloudspeed+=1
        clearclouds()
#game over display
def gameover():
    gameover_text = canvas.create_text(400,200, text='GAME OVER',fill='red',font=('Helvetica',40))
    window.after(3000, window.destroy)

#start
def play():
    sun = canvas.create_oval(50,50,150,150, fill = 'yellow')
    display_area.config(text='Welcome', fg = 'green',bg = 'black')
    
    makeclouds()
    move()



#Adding a button widget
startButton = Button(window, text = 'Start', command = play)
startButton.pack()

#Adding the display area
display_area = Label(window, text='')
display_area.pack() 


canvas.bind_all('<Key>',moveoninput)


window.after(10,updatelevel)
window.after(100,checkhits)

window.mainloop()
