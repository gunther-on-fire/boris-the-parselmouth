n = int(input())
A = [1]

for i in range(n+1):
	print(A)
	A.insert(0,0)
	for j in range(len(A)-1):
		A[j] += A[j+1]



