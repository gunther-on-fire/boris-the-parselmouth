A = list(map(int, input('Расстановка кузнечиков с длинами их прыжков: ').split()))
t = int(input('Число секунд (количество итераций): '))

for i in range(t):
	A.insert(((len(A)-1)-A[-1]), A[-1])
	A.pop()
print(A)
