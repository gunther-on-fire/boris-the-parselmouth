import turtle

turtle.shape('turtle')
turtle.speed(1)

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

l = 300
h = l/6*3**0.5

turtle.penup()
turtle.setpos(-l/2, -h/2)
turtle.pendown()

Helge_Von_Koch(l, 1)
turtle.goto(0, 0)






	