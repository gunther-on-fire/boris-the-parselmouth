import robot
 #создаем робота
r = robot.rmap()
 #загружаем карту соответствующей задачи
r.lm('task11')
r.sleep = 0.01

def change_square(square_dir):
	if square_dir == 'right':
		r.rt()
		return 'down'
	elif square_dir == 'down':
		r.dn()
		return 'left'
	elif square_dir == 'left':
		r.lt()
		return 'up'
	else:
		r.up()
		return 'right'

def squares():
	cur = int(r.gettext())
	r.rt()
	cur += int(r.gettext())
	r.dn()
	cur += int(r.gettext())
	r.lt()
	cur += int(r.gettext())
	r.up()
	return cur

def task():

	min_sum = 37 
	
	r.jumpTo((1,1))
	
	for i in range(5):
		for j in range(2):
			for col in range(1, 14):
				cur_sum = squares()
				if cur_sum < min_sum:
					min_sum = cur_sum
					x = r.getCoordR()
					y = r.getCoordC()
				if col != 13:
					if j == 0:
						r.rt()
					else:
						r.lt()
			if i == 4 and j == 0:
				break
			r.dn()
	r.jumpTo((x,y))
	square_dir = 'right'
	for i in range(4):
		r.pt('yellow')
		square_dir = change_square(square_dir)
r.start(task)
