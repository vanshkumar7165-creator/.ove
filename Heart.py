import turtle
import math
import time

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(1)
pen.color("red")
pen.width(2)
pen.hideturtle()

points = []

for i in range(360):
    t = i * math.pi / 180
    x = 16 * math.sin(t)**3
    y = (13 * math.cos(t)
         - 5 * math.cos(2*t)
         - 2 * math.cos(3*t)
         - math.cos(4*t))
    points.append((x*15, y*15))

for i in range(len(points)):
    pen.penup()
    pen.goto(points[i])
    pen.pendown()
    pen.goto(points[(i * 2) % len(points)])
    time.sleep(0.02)

turtle.done()
