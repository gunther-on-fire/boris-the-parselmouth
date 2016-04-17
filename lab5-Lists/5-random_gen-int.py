from random import *

int_list = open('int_list.txt', 'w')

for i in range(1000000):
	s = randint(0, 100)
	print(s, file=int_list)

int_list.close()
