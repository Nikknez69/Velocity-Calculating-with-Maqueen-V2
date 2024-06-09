# Velocity calculator with maqueen & bbc microbit
from mbrobot_plusV2 import *
from microbit import *
import radio

radio.on()
radio.config(channel=7,group=123)

def get():
    message = radio.receive()
    while message == None:
        message = radio.receive()
    return(message)

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        radio.send("start")
        message = get()
        if message == "ERROR":
            print("Roboter ist zu nah an der Wand!")
        else:
            print("Geschwindigkeit = {}".format(message))
    sleep(10)