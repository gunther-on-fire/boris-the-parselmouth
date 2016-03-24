import turtle
from math import sin, pi

turtle.shape('turtle')

def circle(r, count, sgn):
	a = 2*r*sin(pi/n)
	phi = 180*(1-2/n)
	for i in range(n):
		turtle.forward(a)
		turtle.right(sgn*(180-phi))

r = 20
n = 50 # "точность" окружности
count = 10

turtle.seth(90)	
for circle_quantity in range(count):
	circle(r, count, 1)
	circle(r, count, -1)
	r += 10