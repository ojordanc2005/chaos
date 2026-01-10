from matplotlib import pyplot as plt
import numpy as np

x = [0, 1, 2, 1]
y = [0, 1, 0, -1]

plt.fill(x, y, 'r', alpha=0.5)
plt.title('Basic Matplotlib.pyplot.fill() Example - how2matplotlib.com')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()