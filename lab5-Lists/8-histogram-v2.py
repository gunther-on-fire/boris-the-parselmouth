import matplotlib.pyplot as plt

file = open('float_list.txt', 'r')
A = list(map(float,file))
file.close()

A.sort()
	
_min = A[0]
_max = A[-1]+0.1 #расширение интервала вправо — для случая попадания эл-та списка на границу
N = 20 #количество интервалов
Counts = [0]*N
l = _max - _min

for elem in A:
	i = int((elem -_min)/l*N)
	Counts[i] += 1

plt.bar([A[0]+l/N*k for k in range(N)], Counts, width = l/N)
plt.xticks([A[0]+l/N*k for k in range(N)])
plt.show()
