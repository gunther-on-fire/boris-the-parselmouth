import turtle
from math import sin, pi

turtle.shape('turtle')

n = 50
r = 20
double_leaf = 3 #количество лепестков по два (180/delta)
delta = 0
phi = 180*(1-2/n)
a = 2*r*sin(pi/n)

for angle in range(double_leaf):
	turtle.seth(delta)
	for leaf in range (2):
		for i in range(n):
			turtle.forward(a)
			turtle.left(180-phi)
		phi = 360-phi #смена угла
	delta += 180/double_leaf #угол поворота