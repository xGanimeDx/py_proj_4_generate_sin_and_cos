import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi,np.pi,256,endpoint=True)
sin, cos = np.sin(X), np.cos(X)
plt.plot(X, sin)
plt.plot(X, cos)

plt.show()