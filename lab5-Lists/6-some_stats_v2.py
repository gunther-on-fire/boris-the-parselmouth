input = open('float_list.txt', 'r')

A = []
sum_sqr = 0

for line in input.readlines():
	A.append(line.rstrip())

input.close()

for i in range(len(A)):
	A[i] = float(A[i])

for elem in A:	
	sum_sqr += (elem)**2 

print('Среднее арифметическое: ', sum(A)/len(A)) 
print('Среднеквадратическое отклонение: ',(((sum_sqr - sum(A)**2/len(A))/(len(A)-1))**0.5))
print('Максимальное число: ', max(A)) 
print('Положение max числа: ', A.index(max(A))) 
print('Минимальное число: ', min(A))
print('Положение min числа: ', A.index(min(A)))
