# task2a.py - switch bouncs effect
# Peter Cheung 30 May 2020

from machine import Pin
import time

# instantiate Pin objects
button = Pin(21, Pin.IN, Pin.PULL_UP)

while True:       # Loop forever
    if button.value() == 1:
        print('+', end = '')
        while button.value() == 1:
            pass
        print('-', end = '')

