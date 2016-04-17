import matplotlib.pyplot as plt

Counts = []

file = open('float_list.txt', 'r')
A = list(map(float,file))
file.close()

A.sort()

length = (A[-1]+0.1-A[0])/20 #+0.1 — для расширения интервала справа

for k in range(20):
	count = 0
	for elem in A:
		if elem >= A[0]+length*k and elem < A[0]+length*(k+1):
			count += 1
	Counts.append(count)

plt.bar([A[0]+length*k for k in range(20)], Counts, width = length)
plt.xticks([A[0]+length*k for k in range(20)])
plt.show()
