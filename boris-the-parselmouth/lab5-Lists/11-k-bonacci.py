k = int(input())
n = int(input())
A = []

for i in range(k):
	A.append(1)
for j in range(n-k+1):
	A.append(sum(A[j:j+k]))
print(A[-1])
