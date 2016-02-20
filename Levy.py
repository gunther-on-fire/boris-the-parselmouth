import turtle

turtle.shape('turtle')
turtle.speed('fastest')

def Levy(l, n):
	if n == 0:
		turtle.forward(l)
	else:
		turtle.left(45)
		Levy(l/2**0.5, n-1)
		turtle.right(90)
		Levy(l/2**0.5, n-1)
		turtle.left(45)

l = 300
n = 10

turtle.penup()
turtle.goto(-l/2, -l/(2*(2**0.5+1)))
turtle.pendown()

Levy(l, n)