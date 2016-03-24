import turtle

turtle.shape('turtle')
turtle.speed(5)

def Helge_Von_Koch(l, n):
	if n == 0:
		turtle.forward(l)
	else:
		Helge_Von_Koch(l/3, n-1)
		turtle.left(60)
		Helge_Von_Koch(l/3, n-1)
		turtle.right(120)
		Helge_Von_Koch(l/3, n-1)
		turtle.left(60)
		Helge_Von_Koch(l/3, n-1)

def Kochflake(l, n):
	for i in range (3):
		Helge_Von_Koch(l, n)
		turtle.right(120)

l = 300
h = l/6*3**0.5
n = 3

turtle.penup()
turtle.setpos(-l/2, h)
turtle.pendown()

Kochflake(l, n)

turtle.goto(0, 0)




	