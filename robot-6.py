import robot
 #создаем робота
r = robot.rmap()
 #загружаем карту соответствующей задачи
r.lm('task6')

def task():
	T_x = int(input())
	T_y = int(input())
	x = 0
	y = 0
	for length in range(T_x):
		if r.wr():
			break
		r.pt('yellow')
		x += 1
		if x < T_x:
			r.rt()
	r.lt(int(T_x/2))
	
	for length in range(T_y):
		if r.wd():
			break
		r.pt('yellow')
		y += 1
		if y < T_y:
			r.dn()
	
	if T_x%2 == 0:
		r.rt()
		while y > 1:
			r.pt('yellow')
			r.up()
			y -= 1

r.start(task)