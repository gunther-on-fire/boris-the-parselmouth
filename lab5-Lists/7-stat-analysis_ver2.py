input = open('int_list.txt', 'r')

A = []
B = []
C = []

max_rep = min_rep = None

for line in input.readlines():
	A.append(line.rstrip())

input.close()

for i in range(len(A)):
	A[i] = int(A[i])

for elem in A:
	if elem not in B:
		B.append(elem)

for elem in B:
	count = A.count(elem)
	if (max_rep == None or count > max_rep):
		max_rep = elem
	if (min_rep == None or count < min_rep):
		min_rep = elem

print('The most repetitive value is', max_rep)
print('The least repetitive value is', min_rep)
print("Unique numbers' quantity is", len(B))




