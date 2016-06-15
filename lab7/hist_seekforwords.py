import matplotlib.pyplot as plt

word_length = 0
Dict = []
Hist = []

file = open('ololo.txt', 'r')

for letter in file.read():
	if letter == ' ' or letter == '\n':
		Dict.append(word_length)
		word_length = 0
	else:
		word_length += 1

file.close()
Dict.sort()
print(Dict, len(Dict))
plt.hist(Dict, bins=max(Dict), rwidth=1)
plt.show()
