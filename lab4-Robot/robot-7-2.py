import robot
 #создаем робота
r = robot.rmap()
 #загружаем карту соответствующей задачи
r.lm('task7')
r.sleep = 0.05

def switch_direction(direction):
	if direction == 1:
		return -1
	else:
		return 1

def task():
	direction = 1
	count = 0
	 #начальное положение
	while not r.wl():
		r.lt()
	while not r.wu():
		r.up()

	while count <= 1:
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
		if r.wu() and r.wd():
			count += 1
		else:
		 	count = 0 

	if direction == 1:
		r.lt()
	else:
		r.rt()
		
	while (r.wu() and r.wd()):
			r.pt('yellow')
			if direction == 1:
				r.rt()
			else:
				r.lt() 

r.start(task)