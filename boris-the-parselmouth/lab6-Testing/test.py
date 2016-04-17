A = [-41,42]
min_count = count = len(A)

for i in range(len(A)):
	if A[i] < 0:
		for j in range(i,len(A)):
			print(j)
			if abs(A[i]) == A[j]:
				count = j - i
				break
			else:
				count = 0

	if count < min_count:
		min_count = count

print(min_count)