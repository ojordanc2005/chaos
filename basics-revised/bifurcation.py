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

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

ax.grid()
ax.set_facecolor('black')

resolution = 50
c_range = np.linspace(-2, -0.5, resolution)

def function(x, c):
    return x**2 + c

x = 0
n_iterations = 20

# this doesn't work

'''
# in essence, the characterizing function can be the same as the plotting/iterating one,
# if the plotting one only accepts values within the escape radius

for c in c_range:
    i = 0
    while (i < n_iterations):
        # iterate
        y = function(x, c)
        x = y
        i = i + 1
    if (y < 2 and y > -2):
            ax.scatter(c, y, c='white', marker='.')

plt.show() '''

# original code

'''
def characterize(x, c):
    i = 0
    while (i < 8):
        y = function(x, c)
        x = y
        i = i + 1
        # here's where i put my condition for stability. seeing from the cobweb plot, it seems like iterations
        # only result in inputs less than the initial input, otherwise they blow up to infinity. 
        # thus, I think it's safe to establish the escape radius to the confines of my plot window. 
        if (x > 2 or x < -2):
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

plt.show()'''