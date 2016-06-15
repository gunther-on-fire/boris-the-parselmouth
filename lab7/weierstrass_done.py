
import matplotlib.pyplot as plt
import numpy as np

a = 10
b = 0.1
n = 100
x_values = np.arange(-2.0, 2.0, 0.0025)

@np.vectorize
def f(x):
	return sum((b**i)*np.cos((a**i)*np.pi*x) for i in range(n))

y_values = f(x_values)

plt.plot(x_values, y_values)
plt.show()