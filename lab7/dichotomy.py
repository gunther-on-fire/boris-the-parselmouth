def func(x):
 return x*x-x-6

def dichotomy(a,b,eps):
	while abs(a-b) > 2*eps:
		c = (a+b)/2
		if func(a)*func(c) < 0:
			b = c
		elif func(a)*func(c) > 0:
			a = c
		else:
			break
	print(c)
dichotomy(-4,0,0.01)