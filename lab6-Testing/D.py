k = int(input())
N = int(input())
B = ['x']*N

for year in range(k):
	A = list(map(int, input().split()))
	A = A[:N]
	for i in range(N):
		if B[i] == 'x' or A[i] < B[i]:
			B[i] = A[i]

print(B)