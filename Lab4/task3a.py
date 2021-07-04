# task3a.py

import time
from machine import Pin
from oled import OLED  # load oled module from flash memory
from rotary_irq_esp import RotaryIRQ

oled = OLED()  # Instantiate an OLED object
oled.init_display()

r = RotaryIRQ(pin_num_clk=19,
              pin_num_dt=22,
              min_val=-100,
              max_val=100,
              reverse=True,
              range_mode=RotaryIRQ.RANGE_BOUNDED)

val_old = r.value()
while True:
    val_new = r.value()
    
    if val_old != val_new:              # knob turned
        val_old = val_new
        oled.draw_text(32, 32, '{:4d}'.format(val_new), size=2, space=2)  # each character is 6x8 pixels
        oled.display()  # flush display
        time.sleep_ms(20)


