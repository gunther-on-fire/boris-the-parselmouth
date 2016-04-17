N = int(input('Время работы метрополитена: '))
A = list(map(int,input('Количество пассажиров в час: ').split()))
A = A[:N]
k = int(input('Продолжительность часа пик: '))
max_pass_quantity = 0

for i in range(N-k):
	pass_quantity = sum(A[i:i+k])
	if pass_quantity > max_pass_quantity:
		max_pass_quantity = pass_quantity

print(max_pass_quantity)
