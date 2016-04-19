N = int(input())
A = list(map(int,input().split()))
A = A[:N]

A.sort()
for i in range(len(A)):
	if A[i] == A[i+1]:
		print(A[i])
		break