#App that allows a user to set a plant watering timer that resets if it has rained
from machine import Pin, ADC, PWM, I2C
from time import sleep, sleep_ms
from machine_i2c_lcd import I2cLcd
import utime

#intialize vars for user input
day = 0
hour=0
mins=0

pump_speed=100
pump_time=20

#set buttons to GPIO Pins
btn1 = Pin(4, Pin.IN,Pin.PULL_UP)
btn2 = Pin(3, Pin.IN,Pin.PULL_UP)
btn3 = Pin(2, Pin.IN,Pin.PULL_UP)

#initalize LCD
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)

addr = i2c.scan()[0]
lcd = I2cLcd(i2c, addr, 2, 16)

#initalize water sensor
water_sensor_DO = Pin(0, Pin.IN)
water_sensor_ADC = ADC(0) # GPI26

pwmPIN=16
cwPin=14 
acwPin=15

#moves dc motor that is used to drive water pump
def pump(speed,direction,speedGP,cwGP,acwGP):
  if speed > 100: speed=100
  if speed < 0: speed=0
  Speed = PWM(Pin(speedGP))
  Speed.freq(50)
  cw = Pin(cwGP, Pin.OUT)
  acw = Pin(acwGP, Pin.OUT)
  Speed.duty_u16(int(speed/100*65536))
  if direction < 0:
      cw.value(0)
      acw.value(1)
  if direction == 0:
      cw.value(0)
      acw.value(0)
  if direction > 0:
      cw.value(1)
      acw.value(0)
pump(pump_speed,0,pwmPIN,cwPin,acwPin)

#check if there has been rain
def checkRain():
    if water_sensor_DO.value() == 0:
        print("It is raining: {}".format(water_sensor_ADC.read_u16()))
        return True
    else:
        return False

#gets user input
def getNum(message,top):
    global btn1,btn2,btn3
    num = 0
    end=1
    while(end==1):
        end=btn3.value()
        lcd.putstr(message)
        lcd.putstr(str(num))
        sleep(.2)
        lcd.clear()
        if btn1.value()==0 and num>0:
            num-=1
        if btn2.value()==0 and num<top:
            num+=1
    return num
                
#start screen
lcd.putstr("Press Button\n")
lcd.putstr('To Set ')
while(btn1.value()==1 and btn2.value()==1 and btn3.value()==1):
    btn_status=btn1.value()
    utime.sleep(.2)

def convertDays():
    global day
    day = day*24*60
    
def convertHours():
    global hour
    hour = hour*60
    
#convert time left to days, hours, mins for LCD display
def convertTimeLeft(n):
    txtTimeLeft=[]
    if n>=1440:
        txtTimeLeft.append(n//1440)
        n= n%1400
    else:
        txtTimeLeft.append(0)
    if n>=60:
        txtTimeLeft.append(n//60)
        n=n%60
    else:
        txtTimeLeft.append(0)
    if n>=0:
        txtTimeLeft.append(n)
    else:
        txtTimeLeft.append(0)
    return txtTimeLeft

#collect useer input
day = getNum('DAYS\n',100)
convertDays()
hour = getNum('HOURS\n',24)
convertHours()
mins = getNum('MINUTES\n',60)

cycletime= day+hour+mins
cycles=1
rained = False

#time for user to set timer
inputT=utime.time()

while True:
    currentT = ((utime.time()-inputT)/60)/cycles
    timeLeft=cycletime-currentT
    print(timeLeft)
    print(inputT)
    #display time left to user
    tlist=convertTimeLeft(timeLeft)
    lcd.putstr('DAYS: '+str(int(tlist[0]))+' HOURS: '\
               +str(int(tlist[1]))+' MINS: '+str(round(float(tlist[2]),2)))
    #if there has been rain in a cycle set rained bool to true
    if checkRain() == 1:
        rained = True
    #if user choosen time has passed and it has not rained turn
    #on pump for 20 secs 
    if timeLeft==0 :
        cycles+=1
        if rained == False:
            pump(pump_speed,1,pwmPIN,cwPin,acwPin)
            sleep(pump_time)
            pump(pump_speed,0,pwmPIN,cwPin,acwPin)
            inputT+=(pump_time*4)
        
        rained=False

    utime.sleep(1)
    lcd.clear()

        

        
