def fib(n):
	if n < 2:
		return n
	else:
		return fib(n-2)+fib(n-1)

n = 5

for number in range(n):
	print(fib(number))
	n += 1