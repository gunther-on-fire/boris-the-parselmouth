A = [1,2,3,4,5]

for i in range(1, len(A), 2):
	A.insert(i, A[-1])
	A.pop()
print(A)