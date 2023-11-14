"""Turtle!!!"""
from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

leo.penup()
leo.goto(-125, 125)
leo.pendown()

leo.begin_fill()
#  leo.color(60, 208, 221)
#  leo.pencolor("pink")
#  leo.fillcolor("blue")
leo.color(62, 88, 210)

i: int = 0
while i < 3:
    leo.forward(250)
    leo.right(120)
    i += 1

leo.end_fill()

done()