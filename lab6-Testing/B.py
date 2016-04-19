N = int(input())
A = list(map(int,input().split()))
A = A[:N]
min_coins_number = coins_number = 0

for elem in A:
	if elem == 5:
		coins_number += 1
	else:
		coins_number -= int(elem/5-1)
	if coins_number < min_coins_number:
		min_coins_number = coins_number

if min_coins_number < 0:
	print(abs(min_coins_number))
else:
	print(0)
