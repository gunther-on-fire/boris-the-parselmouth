N = int(input())
k = int(input())

A = [0]*N

for i in range(k):
	B = list(map(int,input().split()))
	B = B[:3]
	A[(B[0] - 1)] -= B[2]
	A[(B[1] - 1)] += B[2]

print(A)