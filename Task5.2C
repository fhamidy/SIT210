from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

##hardware
led = LED(14)
led2 = LED(15)
led3 = LED(18)

##GUI definitions##
win = Tk()
win.title("LED toggle")
myFont = tkinter.font.Font(family='Helvetica',size=12,weight='bold')

###Event Functions###
def ledToggle():
	if led.is_lit:
		led.off()
		ledButton["text"] = "Turn red LED on"
	else:
		led.on()
		ledButton["text"] = "Turn LED off"
		
def led2Toggle():
    if led2.is_lit:
        led2.off()
        ledButton2["text"] = "Turn green LED on"
    else:
        led2.on()
        ledButton2["text"] = "Turn LED off"
        
def led3Toggle():
    if led3.is_lit:
        led3.off()
        ledButton3["text"] = "Turn yellow LED on"
    else:
        led3.on()
        ledButton3["text"] = "Turn LED off"
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()
        
###Widgets###
ledButton = Button(win, text='Turn red LED on', font=myFont,command=ledToggle,bg='bisque2',height=1,width=24)
ledButton2 = Button(win, text='Turn green LED on', font=myFont,command=led2Toggle,bg='bisque2',height=1,width=24)
ledButton3 = Button(win, text='Turn yellow LED on', font=myFont,command=led3Toggle,bg='bisque2',height=1,width=24)
exitButton = Button(win, text='EXIT', font=myFont,command=close,bg='red',height=1,width=6)

ledButton.grid(row=0,column=1)
ledButton2.grid(row=1,column=1)
ledButton3.grid(row=2,column=1)
exitButton.grid(row=3,column=1)




