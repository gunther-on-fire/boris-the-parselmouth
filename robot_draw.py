import robot
 # создаем робота
r = robot.rmap()
 #загружаем карту соотвествующей задачи
r.lm('task2')

def task():
	r.up(1)
	for i in range(5):	
		r.up(1)
		r.rt(1)
		r.pt()
		r.rt(1)
		r.dn(1)
		r.pt()
		r.dn(1)
		r.lt(1)
		r.pt()
		r.lt(1)
		r.up(1)
		r.pt()
		r.rt(3)

r.start(task)