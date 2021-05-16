import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
from time import sleep

GPIO.setmode(GPIO.BCM)
sensor = DistanceSensor(trigger = 18, echo=24) #read distance sensor
GPIO.setup(21, GPIO.OUT) # initialise led output
ana = GPIO.PWM(21,50) # initialise analog output on led with frequency of 50
ana.start(0) # set initial value as 0

while True:
    sleep(2)
    outputData = sensor.distance # read the data
    outputData = round(sensor.distance, 1) # gives a rounded value
    outputDataCM = outputData*100 # convert output to cm value
    ana.ChangeDutyCycle(100-outputDataCM) # closer to 100, btightest light, lower the value, lower the led brightness is
    print(100-outputData)

ana.stop()
GPIO.cleanup()



