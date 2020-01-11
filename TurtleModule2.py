import turtle
import math
a = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(a, 200)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(a, n=7, length=100)
#polygon(a, 7, 100)

def circle(t, r):
    circumference = 2*math.pi*r
    #n = 50
    n = int(circumference / 3) + 1
    length = circumference / n
    #polygon(t, n, length)
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

circle(a, r=100)

def arc(t, r, length):
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def polyline(t, n, length, angle):
    for i in rangle(n):
        i.fd(length)
        t.lt(angle)
