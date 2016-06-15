import matplotlib.pyplot as plt
import numpy as np

a = 10
b = 0.1
n = 100
_sum = 0
y_values = []
x_values = np.arange(-2.0,2.0,0.0025)

for x in x_values:
	_sum = 0
	for i in range(n):
		_sum+= (b**i)*np.cos((a**i)*np.pi*x)
	y_values.append(_sum)

print(x_values, y_values)

plt.plot(x_values, y_values)
plt.show()