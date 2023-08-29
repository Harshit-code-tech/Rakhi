import turtle as t


# Set up the turtle environment
def setup_turtle():
    t.bgcolor("yellow")
    rakhi = t.Turtle()
    rakhi.shape("turtle")
    rakhi.color("blue")
    return rakhi


# Draw the base circle and small circles around it
def draw_base(rakhi):
    rakhi.up()
    rakhi.goto(0, 0)
    rakhi.down()
    rakhi.circle(BASE_RADIUS)

    for i in range(NUM_SMALL_CIRCLES):
        rakhi.up()
        rakhi.setheading(ANGLE_STEP * i)
        rakhi.down()
        rakhi.circle(BASE_RADIUS)


# Draw the central red circle
def draw_center_circle(rakhi):
    rakhi.up()
    rakhi.goto(-40, -CENTER_RADIUS + 30)
    rakhi.down()
    rakhi.begin_fill()
    rakhi.fillcolor("red")
    rakhi.circle(CENTER_RADIUS)
    rakhi.end_fill()


# Draw the ropes around the base
def draw_ropes(rakhi):
    rakhi.up()
    rakhi.goto(0, 127)
    rakhi.down()
    rakhi.left(47)
    rakhi.circle(436, 120)

    rakhi.up()
    rakhi.goto(0, -127)
    rakhi.down()
    rakhi.right(47)
    rakhi.circle(436, -120)


def main():
    rakhi = setup_turtle()

    draw_base(rakhi)
    draw_center_circle(rakhi)
    draw_ropes(rakhi)

    # Write the message
    t.penup()
    t.goto(0, -230)  # Adjusted coordinates for message placement
    t.color("black")
    t.write("Happy Raksha Bandhan meri pyaari behan,\nwhere is my rasogulla?", align="center",
            font=("Arial", 16, "normal"))

    # Keep the turtle window open
    t.done()


# Constants
BASE_RADIUS = 65
NUM_SMALL_CIRCLES = 6
ANGLE_STEP = 360 / NUM_SMALL_CIRCLES

CENTER_RADIUS = 52


if __name__ == "__main__":
    main()
