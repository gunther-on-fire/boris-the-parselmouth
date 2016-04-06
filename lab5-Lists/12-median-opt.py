N = int(input('Количество элементов в списке (нечётное число): '))
A = list(map(int,input().split()))
A = A[:N]

greater_than_count = 0
middle = int((max(A) + min(A))/2)

if middle not in A:
    diff = middle
    for elem in A:    
        cur_diff = abs(elem - middle)
        if cur_diff < diff:
            median = elem
            diff = cur_diff
else:
    median = middle

while True:
    
    greater_than_count = sum(elem < median for elem in A)
    
    if greater_than_count == N//2:
        break
  
    sgn = 1 if greater_than_count > N//2 else -1

    diff = median
    for elem in A:
        cur_diff = sgn*(median - elem)
        if cur_diff < diff and cur_diff > 0:
            new_median = elem
            diff = cur_diff
    median = new_median

print(median)