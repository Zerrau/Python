import autopy
import math
import time
import random
import sys

TWO_IP = math.pi * 2.0
def sine_mouse_wave():
    width,height = autopy.screen.size()
    height /= 2
    height -=10

    for x in range (int(width)):
        y = int(height * math.sin((TWO_IP * x) / width)+ height)
        autopy.mouse.move(x,y)
        time.sleep(random.uniform(0.001,0.003))
sine_mouse_wave()