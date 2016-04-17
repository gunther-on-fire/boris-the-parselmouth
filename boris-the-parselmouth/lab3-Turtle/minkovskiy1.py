import turtle

turtle.shape('turtle')
turtle.speed(5)

def Minkovskiy(l, n):
	if n == 0:
		turtle.forward(l)
	else:
		for angle in [90, -90, -90, 0, 90, 90, -90, 0]:
			Minkovskiy(l/4, n-1)
			turtle.left(angle)

l = 1000

turtle.penup()
turtle.goto(-l/2, 0)
turtle.pendown()

Minkovskiy(l, 4)