A = list(map(int,input().split()))
A = A[:10]

if 2 in A:
	if A[-1] == 2 and A.count(2) == 1:
		print(sum(A)//len(A))
	else:
		A.sort()
		quantity = A.count(2)
		if quantity <= len(A)//2:
			to_be_removed = quantity
		else:
			to_be_removed = len(A) - quantity

		for i in range(to_be_removed):
			A.remove(2)

		print(sum(A)//len(A))
else:
	print(sum(A)//len(A))
