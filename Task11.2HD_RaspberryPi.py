import requests
import RPi.GPIO as GPIO
import time
from smbus import SMBus
from urllib.request import urlopen

addr=0x8
bus=SMBus(1)
base_url = "https://api.thingspeak.com/update?api_key=NPKSYK4LF6RRVUOB"

GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18
led = 40
i=0
max_threshold = 40 # height of mailbox in CM

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(led, GPIO.OUT)
GPIO.output(TRIG, False)

print ("Calibrating.....")
time.sleep(2)

print ("Place the object......")

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        GPIO.output(led, GPIO.LOW)

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start # calculate distance
        distance = pulse_duration * 17150 # convert to CM
        distance = round(distance+1.15, 2) # remove extra decimal points and round value
        thingspeak_up = base_url+"&field1={:.2f}".format(distance)
        
        if distance<=max_threshold and distance>=5:
            requests.post('https://maker.ifttt.com/trigger/motion_detected/with/key/dCZ37XgD9-i3pO2zepxdGV') # sends notification
            print ("distance:",distance,"cm") # to see what the distance is to ensure it outputs correct values
            GPIO.output(led, GPIO.HIGH) # when motion detected, activate led
            i=1
            conn = urlopen(thingspeak_up) # send distance output to graph
            conn.close()
            bus.write_byte(addr,0x1)
        else:
            GPIO.output(led, GPIO.LOW)
            bus.write_byte(addr,0x0)
          
        if distance>max_threshold and i==1:
            print ("place the object....")
            i=0
        time.sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()





