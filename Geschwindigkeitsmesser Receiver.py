# Velocity calculator with maqueen & bbc microbit
from mbrobot_plusV2 import *
from microbit import *
import radio

# initialyzing radio
radio.on()
radio.config(channel=7,group=123)
while True:
    message = radio.receive()
    if message == "start":
        d_0=getDistance()
        if d_0 < 10:
            radio.send("ERROR")
        else:
            t = 3 # how many seconds the robot will drive forward
            forward()
            delay(t*1000)
            stop()
            d_end = getDistance()
            v = (0.01*(d_0-d_end))/t #*0.01 because d_0&d_end are in cm
            radio.send(str(v))
    sleep(10)