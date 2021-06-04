#Particle WEB IDE
#include<Wire.h>
int led = D7;

void setup() {
    Wire.begin(0x8);
    Wire.onReceive(receiveEvent);
    
    
    pinMode(led, OUTPUT);
    digitalWrite(led, LOW);

}

void receiveEvent(int i){
    while (Wire.available()){
        char c = Wire.read();
        digitalWrite(led, c);
    }
}
void loop() {
    delay(1000);
}



#RaspberryPi code

import RPi.GPIO as GPIO
from smbus import SMBus
from tkinter import *
import tkinter.font as tkinterfont

win = Tk()
myFont = tkinterfont.Font(family='Calibri', size=12)

addr=0x8
bus=SMBus(1)

def switchon():
    bus.write_byte(addr,0x1)
def switchoff():
    bus.write_byte(addr,0x0)
def close():
    GPIO.cleanup()
    win.destroy()
    
GUIlabel=Label(win, text='LED toggle i2c')
GUIlabel.grid(row=0, column=1)

onButton = Button(win, text="on LED", font=myFont, command=switchon, bg='green', height=1, width=8)
onButton.grid(row=1, column=1)
onButton = Button(win, text="off LED", font=myFont, command=switchoff, bg='red', height=1, width=8)
onButton.grid(row=2, column=1)
onButton = Button(win, text="finish", font=myFont, command=close, bg='blue', height=1, width=5)
onButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()



