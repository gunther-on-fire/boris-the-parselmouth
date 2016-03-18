import robot
 #создаем робота
r = robot.rmap()
 #загружаем карту соответствующей задачи
r.lm('task8')
r.sleep = 0.05
def switch_direction(direction):
	if direction == 1:
		return -1
	else:
		return 1

def task():
	direction = 1
	cur_height = 0
	height = 0
	hole = 0

	while not r.wd():
		r.dn()
	while not r.wr():
		r.rt()

	while not (r.wu() and r.wl()):
		if r.wl():
			r.up()
			r.lt()
			r.dn()
			while hole < 2:
				if r.wr():
					r.pt('yellow')
					r.dn()
					height += 1
				else:
					hole += 1
					r.dn()
			r.up(2)
			while not r.wl():
				r.pt('yellow')
				r.lt()
			while cur_height < height:
				cur_height += 1
				print(cur_height)
				r.pt('yellow')
				r.up()
			while not r.wr():
				r.pt('yellow')
				r.rt()
			break
		
		if direction == 1:
			if r.wu():
				r.lt()
				direction = switch_direction(direction)
			else:
				r.up()
		else:
			if r.wd():
				r.lt()
				direction = switch_direction(direction)
			else:
				r.dn()

r.start(task)