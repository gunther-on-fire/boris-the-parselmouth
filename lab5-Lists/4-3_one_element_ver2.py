A = [1,2,2,3,3,4,0]
A.sort()
prev_el = None

if A[1] != A[0]:
    print(A[0])
if A[-1] != A[-2]:
    print(A[-1])  

for i in range(1, len(A)-1):		
	if (A[i] != prev_el and A[i] != A[i+1]):
		print(A[i])
	prev_el = A[i]




