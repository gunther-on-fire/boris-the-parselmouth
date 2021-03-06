import turtle
from math import sin, pi

turtle.shape('turtle')
def circle(r, n, angle):
	turtle.seth(angle)
	a = 2*r*sin(pi/n)
	phi = 180*(1-2/n)
	for i in range(int(n/2)+1):
		turtle.forward(a)
		turtle.right(180-phi)

def arc(r_big, r_small, coil_number):
	for coil in range(coil_number):
		circle(r_big, n, angle)
		circle(r_small, n, -angle)
	
r_big = 50
r_small = 10
n = 100
angle = 90
coil_number = 8

l = coil_number*2*r_big+(coil_number-1)*2*r_small

turtle.penup()
turtle.goto(-l/2, -(r_big+r_small)/2)
turtle.pendown()

arc(r_big, r_small, coil_number)