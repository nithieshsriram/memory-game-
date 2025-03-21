from machine import TouchPad, Pin
import time
import random
#ved can you see this
red_pin = TouchPad(Pin(33))
blue_pin = TouchPad(Pin(32))
green_pin = TouchPad(Pin(14))
yellow_pin = TouchPad(Pin(27))

red = Pin(13, Pin.OUT)
blue = Pin(4, Pin.OUT)
green = Pin(12, Pin.OUT)
yellow = Pin(2, Pin.OUT)
buzzer = Pin(18, Pin.OUT)
flag=0
light = [] #1

while (True) :
    print(light)
    for x in light:
        if x == 1:
            red.value(1)
            time.sleep(0.5)
            red.value(0)
            time.sleep(0.5)
        if x == 2:
            blue.value(1)
            time.sleep(0.5)
            blue.value(0)
            time.sleep(0.5)
        if x == 3:
            green.value(1)
            time.sleep(0.5)
            green.value(0)
            time.sleep(0.5)
        if x == 4:
            yellow.value(1)
            time.sleep(0.5)
            yellow.value(0)
            time.sleep(0.5)
    for x in light:
        t=time.time()
        flag2=0
        while(time.time()-t<3):
            if x==1 and red_pin.read() < 500 and blue_pin.read() > 500 and green_pin.read() > 500 and yellow_pin.read() > 500:
                flag2=1
                time.sleep(0.5)
                break
            elif x==2 and blue_pin.read() < 500 and red_pin.read() > 500 and green_pin.read() > 500 and yellow_pin.read() > 500:
                flag2=1
                time.sleep(0.5)
                break
            elif x==3 and green_pin.read() < 500 and blue_pin.read() > 500 and red_pin.read() > 500 and yellow_pin.read() > 500:
                flag2=1
                time.sleep(0.5)
                break
            elif x==4 and yellow_pin.read() < 500 and blue_pin.read() > 500 and green_pin.read() > 500 and red_pin.read() > 500:
                flag2=1
                time.sleep(0.5)
                break

        if(flag2==0):
            print("Fail! Time ran out or incorrect input.")
            buzzer.value(1)
            time.sleep(1)
            buzzer.value(0)
            flag=1
            break

    if flag==1:
       flag=0
       break
    light.append(random.randint(1, 4))
