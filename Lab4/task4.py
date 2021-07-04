# task4.py - Hall Effect Sensor

import time, esp32

from machine import Pin
rLED = Pin (33, Pin.OUT)

THRESHOLD = 65

while True:
    if esp32.hall_sensor() > THRESHOLD:
        rLED.on()
    else:
        rLED.off()
    time.sleep_ms(100)
