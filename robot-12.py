import robot
 #создаем робота
r = robot.rmap()
 #загружаем карту соответствующей задачи
r.lm('task12')
r.sleep = 0.3

def change_direction(d):
	if d == 1:
		return -1
	else:
		return 1

def task():
	col = None
	d = 1
	while col != 1:
		col = r.getCoordC()
		while r.wu():
			if r.wl() or r.wr():
				r.pt('yellow')
				break
			else:
				r.lt()
		if d == 1:
			if r.wu():
				d = change_direction(d)
			else:
				r.up()
		else:
			if r.wl():
				r.dn()
			else:
				r.lt()
				d = change_direction(d)
		
r.start(task)