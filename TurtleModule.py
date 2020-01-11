import turtle
import math

'''
bob = turtle.Turtle()
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
square(bob)
'''

def square(a,l1):
    print(a)
    for i in range(l1):
        a.fd(100)
        a.lt(90)

def polygon(b,l2):
    print(b)
    for i in range(l2):
        b.fd(100)
        b.lt(360/l2)

def circle(t,r):
    print(t)
    circum = 2*math.pi*r
    for i in range(l2):
        b.fd(100)
        b.lt(45)

l1 = int(input("Enter the Length for the Square: "))
l2 = int(input("Enter the Length for the Polygon: "))
r = int(input("Enter the Radius of the Circle: "))
a = turtle.Turtle()
b = turtle.Turtle()
t = turtle.Turtle()
square(a,l1)
polygon(b,l2)
circle(t,r)

turtle.mainloop()
