import math
import RPi.GPIO as GPIO
import time
import pyautogui as pag
import matplotlib.pyplot as plt
import numpy as np
import spiUtils as su

GPIO.setmode(GPIO.BCM)

class Button:
    def button_callback(self, channel):
        pag.press(self.key)
    
    def __init__(self, pinNum, keyToPress):
        self.pin = pinNum
        self.key = keyToPress
        GPIO.setup(pinNum, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pinNum, GPIO.RISING, callback=self.button_callback)
        


### setup buttons ###
# A button (pin 24)
aPin = 24
aButton = 'a'
# B button (pin 25)
bPin = 25
bButton = 'b'

a = Button(aPin, aButton)
b = Button(bPin, bButton)

# setup potentiometer
pot = su.readADC(channel=1)
while True:
    i=0
#for i in range(0, 1000):
 #  # fits potentiometer into range (-1 <-> 1)
  # plusMinusValue = (su.readADC(channel=1)/511.5)-1
   #print(plusMinusValue)
   #time.sleep(.1)
   #i=i+1
   #pag.move(200*plusMinusValue, 0)
