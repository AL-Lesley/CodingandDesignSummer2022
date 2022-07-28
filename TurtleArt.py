import turtle

shelly= turtle.Turtle()
colors = ['red','orange', 'yellow','green','violet','blue'] #creates list of colors
colorsReversed = list(reversed(colors)) #creates a list of colors of the reverse order
x = 2 #sets shelly's initial forward distance
penWidth = 1 #set initial pen width
circleSize=2 #set initial circle size
for i in range(5):
    #Changes circle fill color to 
    for color in colorsReversed:
        shelly.fillcolor(color)
        for color in colors:
            shelly.penup()#stops drawing
            shelly.pencolor(color)#changes pencolor to next in list after every circle
            shelly.width(penWidth)# Width is changed by +.2 for every loop that draws a circle
            penWidth+=.2
            shelly.forward(x)
            shelly.left(30) #shelly turns 30 degrees left after every circle is drawn
            shelly.pendown()
            #circle is filled and drawn
            shelly.begin_fill()
            shelly.circle(circleSize)
            shelly.end_fill()
            circleSize+=.5
            x+=1
