import RPi.GPIO as GPIO
import time
import Tkinter
from Tkinter import *
import tkFont
state = True

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
window = Tk()
myFont = tkFont.Font(family = 'Helvetica', size = 14, weight = 'bold')
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.HIGH)
p = GPIO.PWM(16, 50)
starter = 0
p.start(0)
p.ChangeDutyCycle(100)
window.title("Motor SoundClout.Controller")
window.geometry("500x200")

def exiter():
    GPIO.output(22, GPIO.LOW)
    GPIO.cleanup()
    exit()
def print_value(val):
    global p
    x = float(val)
   ## print (val)
    p.ChangeDutyCycle(x)
    



scale = Tkinter.Scale(orient='horizontal', from_=0, to=100, command=print_value)
scale.pack()

exitButton = Button(window, text = "Exit", font = myFont, command = exiter, height = 1, width = 4)
exitButton.pack()


mainloop()


