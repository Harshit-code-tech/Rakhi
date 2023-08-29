import math
import colorsys
from turtle import *


def heart(k):
    return 15 * math.sin(k) ** 3


def heart1(k):
    return 12 * math.cos(k) - 5 * \
        math.cos(2 * k) - 2 * \
        math.cos(3 * k) - \
        math.cos(4 * k)


def get_color(hue, brightness):
    r, g, b = colorsys.hsv_to_rgb(hue, 1, brightness)
    return r, g, b


speed(1000)
tracer(0, 0)  # Disable screen updates for faster drawing
bgcolor('black')
hue = 0  # Initial hue for color variation

for i in range(6000):
    penup()
    goto(heart(i) * 20, heart1(i) * 20)
    pendown()

    for j in range(5):
        hue += 0.001  # Increment hue for color variation
        brightness = 0.7 + j * 0.05  # Adjust brightness for inner space
        color(get_color(hue, brightness))
        forward(5)
        left(72)

    update()  # Update the screen after drawing each heart section

done()
