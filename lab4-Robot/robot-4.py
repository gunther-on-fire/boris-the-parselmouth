import robot
 #создаем робота
r = robot.rmap()
 #загружаем карту соответствующей задачи
r.lm('task4')

def switch_direction(d):
	if d == 1:
		return -1
	else:
		return 1

def task():
	#начальные условия
	direction = 1
	while not r.wl():
		r.lt()
	while not r.wu():
		r.up()

	while not (r.wr() and r.wd()):
		 if r.label() == 'red':
		 	r.pt('red')

		 if direction == 1:
		 	if r.wr():
		 		direction = switch_direction(direction)
		 		r.dn()
		 	else:
		 		r.rt()
		 else:
		 	if r.wl():
		 		direction = switch_direction(direction)
		 		r.dn()
		 	else:
		 		r.lt()

r.start(task)



