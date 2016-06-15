import numpy as np
import matplotlib.pyplot as plt

f = input('f(x) = ')

x = np.arange(-10,10.01,0.01)
plt.xkcd()
plt.plot(x, eval(f))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.show()
