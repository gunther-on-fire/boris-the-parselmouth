input = open('int_list.txt', 'r')

A = []
B = []
C = []

for line in input.readlines():
	A.append(line.rstrip())

input.close()

for i in range(len(A)):
	A[i] = int(A[i])

#Выделение уникальных элементов

for elem in A:
	if [elem, A.count(elem)] not in B:
		B.append([elem, A.count(elem)])

#Поиск наиболее часто встречающегося и
#наименее часто встречающегося чисел

for i in range(len(B)):
	C.append(B[i][1])

max_count = max(C)
min_count = min(C)

for i in range(len(B)):
	if B[i][1] == max_count:
		max_index = i
		break

for i in range(len(B)):
	if B[i][1] == min_count:
		min_index = i
		break

print(A)
print('The most repetitive value is', B[max_index][0])
print('The least repetitive value is', B[min_index][0])
print("Unique numbers' quantity is", len(B))




