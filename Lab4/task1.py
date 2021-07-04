# task1: Digital output to LED
# rLED - pin 33, gLED - pin 32

from machine import Pin, PWM
import time

rLED = PWM(Pin(33), freq = 1000)
gLED = PWM(Pin(32), freq = 1000)

while True:       # Loop forever
    for i in range(0, 1023, 2):
        rLED.duty(i)
        gLED.duty(i)
        time.sleep_ms(20)

