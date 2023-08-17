import RPi.GPIO as GPIO
from time import sleep as sleep
from time import time as time
import sys

m1_channel = (29,31,33,35)
m2_channel = (32,36,38,40)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(m1_channel, GPIO.OUT)
GPIO.setup(m2_channel, GPIO.OUT)




def goingup(steps):
    a = 0
    while a < steps:
        GPIO.output(m1_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))        
        GPIO.output(m2_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
        sleep(0.01)
        GPIO.output(m1_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))        
        GPIO.output(m2_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
        sleep(0.01)
        GPIO.output(m1_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
        GPIO.output(m2_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
        sleep(0.01)
        GPIO.output(m1_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
        GPIO.output(m2_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
        sleep(0.01)
        a += 1
#    GPIO.output(m1_channel, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))
#    GPIO.output(m2_channel, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))
        

def goingdown(steps):
    a = 0
    while a < steps:
        GPIO.output(m1_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
        GPIO.output(m2_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
        sleep(0.005)
        GPIO.output(m1_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
        GPIO.output(m2_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
        sleep(0.005)
        GPIO.output(m1_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
        GPIO.output(m2_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
        sleep(0.005)
        GPIO.output(m1_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
        GPIO.output(m2_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
        sleep(0.005)
        a += 1
    GPIO.output(m1_channel, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))
    GPIO.output(m2_channel, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))

while True:
    mrot = input('[U]p or [D]own?')
    try:
        a = int(input('Step Count?'))
        if mrot == 'U' or mrot == 'u':
            goingup(a)
        elif mrot == 'D' or mrot == 'd':
            goingdown(a)
        else:
            print('try again dipweed')
    except:
        print('woops')
        