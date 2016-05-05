import robot
 #создаем робота
r = robot.rmap()
 #загружаем карту соответствующей задачи
r.lm('task9')
r.sleep = 0.05

def switch_direction(direction):
	if direction == 1:
		return -1
	else:
		return 1

def task():
	direction = 1
	count = 0

	while not r.wu():
		r.up()
	while not r.wl():
		r.lt()

	while not (r.wr() and r.wd()):
		if direction == 1:
			if r.wr():
				r.dn()
				direction = switch_direction(direction)
			else:
				r.rt()
		else:
			if r.wl():
				r.dn()
				direction = switch_direction(direction)
			else:
				r.lt()
		if r.cl():
			count += 1
	print('The area is', count)
r.start(task)