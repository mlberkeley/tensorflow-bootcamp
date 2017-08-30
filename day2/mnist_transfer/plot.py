import matplotlib.pyplot as plt
import numpy as np

t = np.load('transfer.npy')
r = np.load('rand_weights.npy')

plt.plot(t, 'g')
plt.plot(r, 'r')
plt.show()
