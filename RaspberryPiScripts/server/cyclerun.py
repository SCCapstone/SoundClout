# auth: Foster Williams


import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

sequencefile = open('sequence.txt', 'r')

sequence = sequencefile.read()

sequence = list(sequence)

for x in xrange(0,len(sequence)):
    if (x==0):
        time.sleep(1)
    elif (x==1):
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(22, GPIO.LOW)
