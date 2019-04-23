from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
## hardware
yellow = LED(18)
blue = LED(23)
red = LED(24)

##GUI Definitions##
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica' , size = 12, weight = "bold")

##EVENT FUNCTIONS ##

def toggleLed(led, ledColor, ledButtonText):
        if led.is_lit:
                led.off()
                ledButtonText.set("Turn " +ledColor + " LED on")
        else:
                led.on()
                ledButtonText.set("Turn " +ledColor + " LED off")
def close():
        RPi.GPIO.cleanup()
        win.destroy()

### WIDGETS ###
yellowButtonText = tkinter.StringVar()
yellowButtonText.set('Turn Yellow LED On')
yellowButton = Button(win, font = myFont, textvariable=yellowButtonText, command = lambda: toggleLed(yellow, "Yellow", yellowButtonText), bg = 'bisque2', height = 1, width = 24)
yellowButton.grid(row=0, column=1)
blueButtonText = tkinter.StringVar()
blueButtonText.set('Turn Blue LED On')
blueButton = Button(win,font = myFont, textvariable=blueButtonText,  command =  lambda: toggleLed(blue, "Blue", blueButtonText), bg = 'bisque2', height = 1, width = 24)
blueButton.grid(row=1, column=1)
redButtonText = tkinter.StringVar()
redButtonText.set('Turn Red LED On')
redButton = Button(win,font = myFont, textvariable=redButtonText,  command =  lambda: toggleLed(red, "Red",redButtonText), bg = 'bisque2', height = 1, width = 24)
redButton.grid(row=2, column=1)

## EXIT BUTTON ##

exitButton = Button(win,text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close) #exit cleanly

win.mainloop() #loop forever

