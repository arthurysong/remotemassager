import time, gc, os
import adafruit_dotstar
import board
import feathers2
import digitalio

# Create a DotStar instance
dotstar = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.5, auto_write=True)

# base = digitalio.DigitalInOut(board.D7)
# base.direction = digitalio.Direction.OUTPUT
pin = digitalio.DigitalInOut(board.D7)
pin.direction = digitalio.Direction.OUTPUT

# Turn on the second LDO that drives the Dotstar
feathers2.enable_LDO2( True )

# Say hello
print("\nHello from FeatherS2!")
print("---------------------\n")

# Show available memory
print("Memory Info - gc.mem_free()")
print("---------------------------")
print("{} Bytes\n".format(gc.mem_free()))

flash = os.statvfs('/')
flash_size = flash[0] * flash[2]
flash_free = flash[0] * flash[3]
# Show flash size
print("Flash - os.statvfs('/')")
print("---------------------------")
print("Size: {} Bytes\nFree: {} Bytes\n".format(flash_size, flash_free))

print("Dotstar Time!\n")

# Create a colour wheel index int
color_index = 0

# Rainbow colours on the Dotstar
while True:
    # print("hi")
    # Get the R,G,B values of the next colour
    r,g,b = feathers2.dotstar_color_wheel( color_index )
    # Set the colour on the dotstar
    dotstar[0] = ( r, g, b, 0.5)
    # Increase the wheel index
    color_index += 1
    
    # if color_index == 255:
    #     color_index = 0
    #     feathers2.blink()
    # base.value = True
    # feathers2.blink()
    # time.sleep(5)

    # Sleep for 20ms so the colour cycle isn't too fast
    # time.sleep(0.015)
    
