import robot
 #создаем робота
r = robot.rmap()
 #загружаем карту соответствующей задачи
r.lm('task10')
r.sleep = 0.1

def switch_direction():
	if not r.wd():
		return 'down'
	elif not r.wl():
		return 'left'
	elif not r.wr():
		return 'right'

def cell_to_be_painted(direction):
	if (direction == 'down' and (not r.wl() or not r.wr()) and not r.wd()) or \
	(direction == 'left' and (not r.wu() or not r.wd()) and not r.wl()) or \
	(direction == 'right' and (not r.wu() or not r.wd()) and not r.wr()):
		r.pt('yellow')

def task():
	direction = 'right'
	while not (r.wl() and r.wr() and r.wd()):
		if direction == 'right':
			r.rt()
			cell_to_be_painted(direction)
			if r.wr():
				direction = switch_direction()
		elif direction == 'down':
			r.dn()
			cell_to_be_painted(direction)
			if r.wd():
				direction = switch_direction()
		elif direction == 'left':
			r.lt()
			cell_to_be_painted(direction)
			if r.wl():
				direction = switch_direction()
		print(direction)
r.start(task)

