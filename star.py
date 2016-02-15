import turtle

turtle.shape("turtle")

def star(r,n):
	for i in range(n):
		angle = 180/n
		turtle.forward(r)
		turtle.right(180-angle)

r = 100
star(r,11)