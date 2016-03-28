from random import *

float_list = open('float_list.txt', 'w')

for i in range(1000000):
	s = 100*random()
	print(s, file=float_list)

float_list.close()
