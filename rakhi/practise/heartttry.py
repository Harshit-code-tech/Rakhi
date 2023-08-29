import math
import colorsys
import turtle
import time
import random
from turtle import *


# Basic Song class for demonstration (comment out if not needed)
class Song:
    def __init__(self, title):
        self.title = title

    def play(self):
        print(f"Playing: {self.title}")


# Define the display_typewriter_text function
def display_typewriter_text(message, x, y, font, color):
    penup()
    goto(x, y)
    pendown()
    turtle.color(color)  # Set the text color
    for char in message:
        write(char, align="center", font=font)
        update()
        time.sleep(0.05)  # Delay between typing each character


turtle.hideturtle()


# New enhancement: Animated Background - Draw twinkling stars
def draw_star(x, y, size):
    penup()
    goto(x, y)
    pendown()
    color('white')
    for _ in range(5):
        forward(size)
        right(144)


# New enhancement: Color Variation - Smoothly transition colors using sinusoidal functions
def get_color(hue, brightness):
    r, g, b = colorsys.hsv_to_rgb(hue, 0.5 + 0.5 * math.sin(hue * 10), brightness)
    return r, g, b


# New enhancement: Particle Effects - Add glowing particles that follow heart paths
def draw_particle(x, y):
    penup()
    goto(x, y)
    pendown()
    color(get_color(random.random(), 0.7))  # Set random glowing color
    dot_size = random.randint(2, 5)  # Random size for the particle
    dot(dot_size)  # Draw the glowing particle


# New enhancement: Floating Hearts - Add smaller hearts that move across the screen
def draw_floating_heart(x, y):
    bgcolor('orange')
    penup()
    goto(x, y)
    pendown()
    color('red')  # Set heart color
    begin_fill()
    for _ in range(3):  # Draw a triangular heart shape
        forward(10)
        right(140)
    end_fill()


# Number of floating hearts
num_hearts = 20

# Generate random positions for floating hearts and draw them
for _ in range(num_hearts):
    x = random.randint(-500, 500)
    y = random.randint(-300, 300)
    draw_floating_heart(x, y)

# Generate random particle positions along heart paths and draw particles
for _ in range(num_hearts * 5):
    x = random.randint(-500, 500)
    y = random.randint(-300, 300)
    draw_particle(x, y)


def heart(k):
    return 15 * math.sin(k) ** 3


def heart1(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)


speed(1000)
tracer(0, 0)  # Disable screen updates for faster drawing
bgcolor('black')
hue = 0  # Initial hue for color variation

message_delay = 10  # Display message after 10 seconds
message_iteration = 500  # Display message after this many heart iterations
heart_count = 0
heart_multiplier = 20  # Heart multiplier used in the heart drawing

start_time = time.time()  # Record the start time

# New enhancement: Animated Background - Draw twinkling stars in the background
num_stars = 100
for _ in range(num_stars):
    x = random.randint(-500, 500)
    y = random.randint(-300, 300)
    size = random.randint(1, 3)
    draw_star(x, y, size)

while True:
    penup()
    goto(heart(hue) * heart_multiplier, heart1(hue) * heart_multiplier)
    pendown()

    for j in range(5):
        hue += 0.001  # Increment hue for color variation
        brightness = 0.7 + j * 0.05  # Adjust brightness for inner space
        color(get_color(hue, brightness))
        forward(5)
        left(72)

    update()  # Update the screen after drawing each heart section

    heart_count += 1
    if heart_count >= message_iteration:
        if time.time() - start_time >= message_delay:
            penup()
            text = "Something special for my sister\nHappy Raksha Bandhan!"
            goto(0, 0)  # Position the text in the center
            color('red')  # Set text color to red
            fontsize = int(heart_multiplier * 0.8)  # Adjust font size
            write(text, align="center", font=("Arial", fontsize, "normal"))
            update()  # Update the screen with the text
            break

# Wait for 3 seconds after displaying the text
time.sleep(3)

# Keep the turtle graphics window open for interaction
done()
