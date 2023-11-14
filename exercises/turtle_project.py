"""Turtle Project!"""

__author__ = "730671567"

from turtle import Turtle, colormode, done


def main() -> None:
    """The entrypoint of the Turtle."""
    turty: Turtle = Turtle()
    grass(turty, -500, 0)
    square(turty, -75, 78, 80)
    triangle(turty, -75, 80, 25)
    triangle(turty, -55, 80, 25)
    triangle(turty, -35, 80, 25)
    triangle(turty, -15, 80, 25)
    triangle(turty, 5, 80, 25)
    triangle(turty, -35, 145, 75)
    man(turty, 40, 17)
    turty.hideturtle()
    done()


def square(turt: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square at a specified location (top left corner at x, y) with a specified width."""
    colormode(255)
    turt.color("red")
    turt.penup()
    turt.goto(x, y)
    turt.setheading(0.0)
    turt.pendown()
    i: int = 0
    while i < 4:
        turt.forward(width)
        turt.right(90)
        i += 1


def triangle(turt: Turtle, x: float, y: float, w: float,) -> None:
    """Draws a triangle with the point being at point (x, y)."""
    colormode(255)
    turt.color(195, 120, 180)
    turt.penup()
    turt.goto(x, y)
    turt.setheading(0.0)
    turt.pendown()
    turt.right(60)
    i: int = 0
    while i < 3:
        turt.forward(w)
        turt.right(120)
        i += 1


def grass(turt: Turtle, x: float, y: float) -> None:
    """Draws grass as a base for the beautiful picture at the specified location (x, y)."""
    turt.speed(5000)
    colormode(225)
    turt.color("green")
    turt.begin_fill()
    turt.penup()
    turt.goto(x, y)
    turt.setheading(0.0)
    turt.pendown()
    turt.forward(1000)
    turt.right(90)
    turt.forward(1000)
    turt.right(90)
    turt.forward(1000)
    turt.right(90)
    turt.forward(1000)
    turt.end_fill()


def man(turt: Turtle, x: float, y: float) -> None:
    """Draws a man at the specified location (x, y)."""
    colormode(255)
    turt.color(65, 100, 130)
    turt.penup()
    turt.goto(x, y)  # The hips area of the man
    turt.setheading(0.0)
    turt.pendown()
    turt.right(75)
    turt.forward(50 / 3)
    turt.penup()
    turt.goto(x, y)
    turt.setheading(0.0)
    turt.pendown()
    turt.right(105)
    turt.forward(50 / 3)
    turt.penup()
    turt.goto(x, y)
    turt.setheading(0.0)
    turt.pendown()
    turt.left(90)
    turt.forward(75 / 3)
    turt.penup()
    turt.goto(x, y + 75 / 3)
    turt.setheading(0.0)
    turt.pendown()
    turt.circle(25 / 3)
    turt.penup()
    turt.goto(x, y + 50 / 3)
    turt.setheading(0.0)
    turt.pendown()
    turt.right(55)
    turt.forward(35 / 3)
    turt.penup()
    turt.goto(x, y + 50 / 3)
    turt.setheading(0.0)
    turt.left(235)
    turt.pendown()
    turt.forward(35 / 3)
    
    
if __name__ == "__main__":
    main()
    