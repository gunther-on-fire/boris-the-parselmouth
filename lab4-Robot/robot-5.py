import robot
 #создаем робота
r = robot.rmap()
 #загружаем карту соответствующей задачи
r.lm('task5')

def cell_to_paint(col, row):
	if (row%3 == 1 and col%2 == 1) or \
	(row%3 == 2 and col%2 == 0):
		r.pt('yellow')

def switch_direction(direction):
	if direction == 1:
		return -1
	else:
		return 1

def task():
	direction = 1
	col = 1
	row = 1
	while not (r.wd() and r.wr()):
		cell_to_paint(col, row)
		
		if direction == 1:
			if r.wr():
				r.dn()
				row += 1
				direction = switch_direction(direction)
			else:
				r.rt()
				col += 1
		else:
		 	if r.wl():
		 		r.dn()
		 		row += 1
		 		direction = switch_direction(direction)
		 	else:
		 		r.lt()
		 		col -= 1

r.start(task)
