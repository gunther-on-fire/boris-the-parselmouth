import robot
 #создаем робота
r = robot.rmap()
 #загружаем карту соответствующей задачи
r.lm('task13')
r.sleep = 0.1

def change_direction(d):
	if d == 1:
		return -1
	else:
		return 1

def task():
	
	d = 1
	y = y0 = x = x0 = None
	r.jumpTo((1, 1))
	col = r.getCoordC()

	while (not r.wr() or (not r.wl and c != 1)):
		col = r.getCoordC()
		if d == 1:
			if r.wd():
				r.rt()
				d = change_direction(d)
			else:
				r.dn()
		else:
			if r.wu():
				r.rt()
				d = change_direction(d)
			else:
				r.up()

	if r.wr():
		x0 = r.getCoordR()
		y0 = r.getCoordC()
		while r.wr():
			if d == 1:
				r.dn()
			else:
				r.up()
		x = r.getCoordR()
		while not r.wr():
			r.rt()
		y = r.getCoordC()
		print ('Высота = ', abs(x - x0), 'Расстояние = ', y - y0)
	
	else:
		x0 = r.getCoordR()
		y0 = r.getCoordC()
		while r.wl():
			if d == 1:
				r.dn()
			else:
				r.up()
		x = r.getCoordR()
		while not r.wr():
			r.rt()
		y = r.getCoordC()
		print ('Высота = ', abs(x - x0), 'Расстояние = ', y - y0)
	
r.start(task)