import turtle
import math

turtle.shape('turtle')

def RegPolygon(r,n):
		b = 180*(1-2/n)
		turtle.right(180-b/2)
		a = 2*r*math.sin(math.pi/n)
		
		for i in range(n):
			turtle.forward(a)
			turtle.right(180-b)
r = 20
n = 3
step = 10

for i in range (10):
	turtle.penup()
	turtle.seth(90)
	turtle.forward(step)
	turtle.pendown()
	RegPolygon(r, n)
	
	n += 1
	r += step