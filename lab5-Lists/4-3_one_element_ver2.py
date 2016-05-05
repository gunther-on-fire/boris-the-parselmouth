A = [1,1,2]
A.sort()

if A[1] != A[0]:
    print(A[0])
if A[-1] != A[-2]:
    print(A[-1])  

for i in range(1, len(A)-1):		
	if (A[i] != A[i-1] and A[i] != A[i+1]):
		print(A[i])




