from matplotlib import pyplot as plt
import numpy as np

# this revised version of the logistic bifurcation diagram will take advantage
# of the concept of an escape radius as the condition for instability...
# hopefully, this will result in faster code that can achieve a higher resolution

# another goal of this code is to investigate new means for plotting more generally.
# a way to directly manipulate image pixels rather than making scatterplots would be ideal. 
# fastplotlib and taichi lang are two options I'd like to explore.  
# other options: bokeh, plotly, ...

# first though, optimizing my method!

# establishing the figure
fig = plt.figure()
ax = plt.axes()

ax.grid()
ax.set_facecolor('black')

c_range = np.linspace(-2,-0.25,50)

def function(x, c):
    return x**2 + c

x = 0

def characterize(x, c):
    i = 0
    while (i < 50):
        y = function(x, c)
        x = y
        i = i + 1
        if (x > 5 or x < -5):
            y = 123
            break
    return y

for c in c_range:
    y = characterize(0, c)
    if (y != 123):
        i = 0
        while (i < 50):
            x = y
            y = function(x, c)
            i = i + 1
            if (y < 2 and y > -2):
                ax.scatter(c, y, c='white', marker='.')
            else:
                break

plt.show()