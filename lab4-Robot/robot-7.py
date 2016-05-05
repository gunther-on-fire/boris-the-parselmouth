import robot
 #создаем робота
r = robot.rmap()
 #загружаем карту соответствующей задачи
r.lm('task7')

def switch_direction(direction):
	if direction == 1:
		return -1
	else:
		return 1

def task():
	direction = 1
	count = 0

	while not r.wl():
		r.lt()
	while not r.wu():
		r.up()

	while not (r.wd() and r.wr()):
		if r.wu() and r.wd():
			count += 1
		if (r.wu() and r.wd()) and count > 1:
			r.pt('yellow') 
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

r.start(task)