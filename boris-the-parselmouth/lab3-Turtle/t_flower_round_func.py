import turtle
from math import sin, pi

turtle.shape('turtle')

r = 20
n = 50 # "точность" окружности
double_leaf = 3 #количество двойных лепестков
a = 2*r*sin(pi/n)
phi = 180*(1-2/n)

def circle(sgn):
    for i in range(n):
        turtle.forward(a)
        turtle.left(sgn*(180-phi))

for i in range(double_leaf):
    circle(1)
    circle(-1)
    turtle.left(180/double_leaf)