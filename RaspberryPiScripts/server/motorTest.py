import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(22, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)

print "testing on"

time.sleep(5)

print "testing off"

GPIO.output(22, GPIO.LOW)
GPIO.cleanup()
exit()
