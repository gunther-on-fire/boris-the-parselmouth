import matplotlib.pyplot as plt
import numpy as np

a = 10
b = 0.1
n = 100
y_values = []
x_values = np.arange(-2.0,2.0,0.0025)

for x in x_values:
	y = sum((b**i)*np.cos((a**i)*np.pi*x) for i in range(n))
	y_values.append(y)

plt.plot(x_values, y_values)
plt.show()