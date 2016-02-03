n = int(input())
max = n
max2 = 0
while n != 0:
    n = int(input())
    if n >= max:
        max2 = max
        max = n
    else:
        if n > max2:
            max2 = n
print(max2)