import robot
 # создаем робота
r = robot.rmap()
 #загружаем карту соответствующей задачи
r.lm('task3')

def task():
	for i in range(3):
		r.rt(2)
		r.dn()
		r.up()
	r.rt(2)

r.start(task)