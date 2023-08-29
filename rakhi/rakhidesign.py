import time
import turtle
import math
import random
from turtle import *

# First code: Drawing Om symbol between four diyas
bgcolor("white")
speed(10)
width(40)
pencolor("orangered")
penup()
setpos(-200, 150)
pendown()
left(60)
circle(-120, 230)
bgcolor("grey")
left(160)
circle(-130, 230)
fd(180)
bgcolor("black")
penup()
setpos(-20, -24)
pendown()
left(60)
circle(90, -80)
bgcolor("Violet")
fd(-130)
circle(-70, -170)
back(320)
circle(-70, -170)
back(190)
bgcolor("orange")
penup()
setpos(-60, 300)
pendown()
rt(170)
circle(120, 160)
bgcolor("skyblue")
penup()
setpos(90, 270)
pendown()
circle(30, 360)
color("black")
penup()

clear()
reset()


def set_background_gradient(color1, color2):
    screen = turtle.Screen()
    screen.bgcolor(color1)
    screen.bgcolor(color2)


def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_star(color, size, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x - size / 2, y - size / 2)
    turtle.pendown()
    turtle.begin_fill()

    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

    turtle.end_fill()


def draw_sparkles(radius, num_sparkles):
    for angle in range(0, 360, 360 // num_sparkles):
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        for _ in range(5):
            turtle.forward(10)
            turtle.right(144)


def draw_diya(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Draw the diya body (triangle)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(20)
        turtle.left(120)
    turtle.end_fill()

    # Draw the diya flame
    turtle.penup()
    turtle.goto(x + 10, y + 20)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()


def draw_flower(x, y, petal_color, center_color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Draw petals
    turtle.color(petal_color)
    turtle.begin_fill()
    for _ in range(12):
        turtle.forward(10)
        turtle.left(30)
        turtle.forward(10)
        turtle.left(150)
    turtle.end_fill()

    # Draw center of the flower
    turtle.penup()
    turtle.goto(x, y - 10)  # Position below petals
    turtle.pendown()
    turtle.color(center_color)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()


def draw_rakhi():
    # Set up Turtle
    turtle.speed(10)
    # Set a gradient background
    set_background_gradient("lightcyan", "deepskyblue")

    # Draw the outer circle
    draw_circle("lightpink", 60, 0, 0)

    # Draw decorative shapes as sparkles on the outer circle
    draw_sparkles(50, 12)

    # Draw the central circular base
    draw_circle("red", 40, 0, 0)

    # Draw the star decoration
    draw_star("gold", 20, 0, 10)

    # Draw decorative circles
    for angle in range(0, 360, 30):
        x = 30 * math.cos(math.radians(angle))
        y = 30 * math.sin(math.radians(angle))
        draw_circle("blue", 6, x, y)
        # Draw Rakhi threads between the central circle and the outer circle
        num_threads = 8
        for angle in range(0, 360, 360 // num_threads):
            x1 = 40 * math.cos(math.radians(angle))
            y1 = 40 * math.sin(math.radians(angle))
            x2 = 60 * math.cos(math.radians(angle))
            y2 = 60 * math.sin(math.radians(angle))

            turtle.penup()
            turtle.goto(x1, y1)
            turtle.pendown()
            turtle.color('#8B0000')  # Rakhi thread color
            turtle.goto(x2, y2)
    # Inside the draw_rakhi function
    for angle in range(0, 360, 10):
        x = 60 * math.cos(math.radians(angle))
        y = 60 * math.sin(math.radians(angle))
        draw_circle("orange", 2, x, y)
    # Inside the draw_rakhi function
    for angle in range(0, 360, 30):
        x = 55 * math.cos(math.radians(angle))
        y = 55 * math.sin(math.radians(angle))
        gem_color = random.choice(["red", "blue", "green", "purple"])
        draw_circle(gem_color, 2, x, y)

    # Draw diyas in corners
    draw_diya("brown", -280, 280)  # Top-left corner
    draw_diya("brown", 280, 280)  # Top-right corner
    draw_diya("brown", -280, -280)  # Bottom-left corner
    draw_diya("brown", 280, -280)  # Bottom-right corner

    # Draw improved flowers around the Rakhi
    flower_colors = ["red", "purple", "pink", "orange"]
    for angle in range(0, 360, 45):
        x = 80 * math.cos(math.radians(angle))
        y = 80 * math.sin(math.radians(angle))
        petal_color = random.choice(flower_colors)
        center_color = random.choice(flower_colors)
        draw_flower(x, y, petal_color, center_color)

    # Hide the Turtle
    turtle.hideturtle()

    # Draw a larger rectangular banner for the message
    banner_width = 500  # Increased width
    banner_height = 80  # Increased height
    banner_x = -banner_width / 2
    banner_y = 280  # Adjusted y-coordinate for banner placement
    turtle.penup()
    turtle.goto(banner_x, banner_y)
    turtle.pendown()
    turtle.fillcolor("red")  # Banner background color
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(banner_width)
        turtle.left(90)
        turtle.forward(banner_height)
        turtle.left(90)
    turtle.end_fill()

    # Write the message on the banner
    text_y_offset = 15  # Adjusted y-offset for text placement
    turtle.penup()
    turtle.goto(0, banner_y + banner_height / 2 - text_y_offset)
    turtle.color("blue")  # Text color
    turtle.write(
        "Happy Raksha Bandhan meri pyaari behan,\nwhere is my rasogulla?",
        align="center",
        font=("Arial", 16, "normal")
    )
    turtle.penup()
    turtle.goto(0, -80)  # Adjusted position
    turtle.pendown()
    turtle.color("green")
    turtle.write(
        "Siblings Forever",
        align="center",
        font=("Arial", 12, "normal")
    )


# Draw the Rakhi
draw_rakhi()
# Close the turtle window after 3 seconds
time.sleep(3)
turtle.bye()
