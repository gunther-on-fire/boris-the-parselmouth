import robot
 # создаем робота
r = robot.rmap()
 #загружаем карту соответствующей задачи
r.lm('task2')

def vertical_move(r, move):
	if move == 1:
		r.up()
	else:
		r.dn()
 #задаём направление движение робота
def robot_direction(col):
	if col % 2 == 1:
		return 1
	else:
		return -1

def vertical_move_limit(r, move):
    return (r.wu() and move == 1) or (r.wd() and move == -1)

def task():
	#исходное положение
	col = 1
	row = 3
	move = robot_direction(col)
	
	while True:
		if (col % 3 == 2 and (row == 1 or row == 3)) or \
		((col % 3 == 1 or col % 3 == 0) and row == 2):
			r.pt()
		if vertical_move_limit(r, move):
			if r.wr():
				break
			r.rt()
			col += 1
			move = robot_direction(col)
		else:
			vertical_move(r, move)
			row -= move
r.start(task)
