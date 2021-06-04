import RPi.GPIO as GPIO
import time
from tkinter import *

LED = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

gui = Tk()
gui.geometry("300x50")
gui.title("String to Morse")

txInp = StringVar() 
unit =  0.25

def dot():
	GPIO.output(LED, True)
	time.sleep(unit)
	GPIO.output(LED, False)
	time.sleep(unit)


def dash():
	GPIO.output(LED, True)
	time.sleep(unit*3)
	GPIO.output(LED, False)
	time.sleep(unit)


def newChar():
	time.sleep(unit*2)


def A():
	dot()
	dash()

def B():
	dash()
	dot()
	dot()
	dot()
	
def C():
	dash()
	dot()
	dash()
	dot()

def D():
	dash()
	dot()
	dot()
	
def E():
	dot()

def F():
	dot()
	dot()
	dash()
	dot()

def G():
	dash()
	dash()
	dot()
	
def H():
	dot()
	dot()
	dot()
	dot()
	
def I():
	dot()
	dot()
	
def J():
	dot()
	dash()
	dash()
	dash()
	
def K():
	dash()
	dot()
	dash()
	
def L():
	dot()
	dash()
	dot()
	dot()
	
def M():
	dash()
	dash()
	
def N():
	dash()
	dot()
	
def O():
	dash()
	dash()
	dash()
	
def P():
	dot()
	dash()
	dash()
	dot()
	
def Q():
	dash()
	dash()
	dot()
	dash()
	
def R():
	dot()
	dash()
	dot()
	
def S():
	dot()
	dot()
	dot()

def T():
	dash()
	
def U():
	dot()
	dot()
	dash()
	
def V():
	dot()
	dot()
	dot()
	dash()
	
def W():
	dot()
	dash()
	dash()
	
def X():
	dash()
	dot()
	dot()
	dash()

def Y():
	dash()
	dot()
	dash()
	dash()
	
def Z():
	dash()
	dash()
	dot()
	dot()


def convertToCode():
	MorseText = txInp.get()
	if len(MorseText) > 12:
		return
	for i in MorseText:
		if i.upper() == "A":
			A()
		elif i.upper() == "B":
			B()
		elif i.upper() == "C":
			C()
		elif i.upper() == "D":
			D()
		elif i.upper() == "E":
			E()	
		elif i.upper() == "F":
			F()
		elif i.upper() == "G":
			G()
		elif i.upper() == "H":
			H()
		elif i.upper() == "I":
			I()
		elif i.upper() == "J":
			J()
		elif i.upper() == "K":
			K()
		elif i.upper() == "L":
			L()
		elif i.upper() == "M":
			M()
		elif i.upper() == "N":
			N()
		elif i.upper() == "O":
			O()
		elif i.upper() == "P":
			P()
		elif i.upper() == "Q":
			Q()
		elif i.upper() == "R":
			R()
		elif i.upper() == "S":
			S()
		elif i.upper() == "T":
			T()
		elif i.upper() == "U":
			U()
		elif i.upper() == "V":
			V()
		elif i.upper() == "W":
			W()
		elif i.upper() == "X":
			X()
		elif i.upper() == "Y":
			Y()
		elif i.upper() == "Z":
			Z()
		newChar()

textEntry = Entry(gui, width=12, textvariable=txInp)
convertButton = Button(gui, text="Convert to Morse", command=convertToCode)

textEntry.pack(side=LEFT)
convertButton.pack(side=RIGHT)

gui.mainloop()





