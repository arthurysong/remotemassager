import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut
import time
# import pulseio
import math

switch = DigitalInOut(board.D9)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

base = AnalogOut(board.A0)
# base = pulseio.PWMOut(board.A0)
# base = pulseio.PWMOut(board.A0)


def handle_mode(mode):
    print("mode is ", mode);

mode = 0
while True:
    # value goes from 13550 to 65535
    # base.value = 13550
    # if not switch.value:
    #     base.value = 65535
    # else:
    #     base.value = 0
    # base.value = 65535
    # print("Hello world!")
    # x = 20000
    # while (x <= 65435):
    #     x = x + 10
    #     base.value = x
    #     print("X", x)
    x = 0
    if not switch.value:
        mode = mode + 1
        handle_mode(mode)

    
    # My SIN WAVE repeat
    # while (x <= 6.2832):
    #     y = abs(math.sin(x)) * 51985 + 13550
    #     print("y", y)
    #     base.value = int(y)
    #     print("x", x)
    #     x = x + 0.01

    


    base.value = 0
    # time.sleep(2)
