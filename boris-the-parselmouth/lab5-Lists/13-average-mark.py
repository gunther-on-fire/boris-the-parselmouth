import math

A = list(map(int,input().split()))
A = A[:10]

s = 0
c = 1

for i in range(9):
    if A[i] != 2 or A[i+1] == 2:
        s += A[i]
        c += 1

s += A[9]
print(math.floor(s/c))