import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut
import time
import pulseio
import feathers2

switch = DigitalInOut(board.D9)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

base = AnalogOut(board.A0)
# base = pulseio.PWMOut(board.A0)
led = DigitalInOut(board.)

feathers2.led_blink()
while True:

    # base.duty_cycle = 65535
    # base.value = 65535
    if not switch.value:
        base.value = 65535
        # base.duty_cycle = 65535
    else:
        base.duty_cycle = 0
