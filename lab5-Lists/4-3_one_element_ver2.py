A = [1,2,2,3,3,4,0]
A.sort()
prev_el = None

for i in range(len(A)):
	if i == 0:
		if A[1] != A[0]:
			print(A[0])
	elif i == len(A):
		if A[len(A)] != A[len(A)-1]:
			print(A[len(A)])		
	else:
		if (A[i] != prev_el and A[i] != A[i+1]):
			print(A[i])
		prev_el = A[i]




