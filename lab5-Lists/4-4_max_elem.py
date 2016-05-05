A = [5,1,2,5,2,3,5,3,4,0,5,5]

max_count = 0

for element in A:
	count = A.count(element)
	if count > max_count:
		max_count = count
		max_element = element
		count = 0
print(max_element)
