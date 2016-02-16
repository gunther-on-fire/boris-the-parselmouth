import turtle
from math import pi, cos

turtle.shape("turtle")
turtle.speed(1)

def star(r,n):
	angle = 180/n
	l = 2*r*cos(pi/(2*n))

	turtle.penup()
	turtle.seth(90)
	turtle.forward(r)
	turtle.right(180-angle/2)
	turtle.pendown()

	for i in range(n):
		turtle.forward(l)
		turtle.right(180-angle)

r = 150

star(r,11)
turtle.goto(0,0) #проверка центра звезды