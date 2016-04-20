f = open('input.txt', 'r')
A = list(map(int, input.readline().split()))
f.close()

A.sort()
i = 1
while A[i] != A[i - 1]:
	i += 1

f = open('output.txt', 'w')
print(A[i-1], file=f)
f.close()