from matplotlib import pyplot as plt
import numpy as np

# this will basically do what iteration.py does for n_iteration of like 100 for a range of c values

c_range = np.linspace(-2,-0.25,50)

# i want to make a scatter plot

# what is stable and unstable equilibria? this is an interesting problem

# you first iterate a bunch for a given c-value to let the orbit find its "characteristic behavior"

#again, the function
def function(x, c):
    return x**2 + c

# seed of 0
x = 0
# this function is poorly named (or maybe poorly used) and iterates 100 times for a given c value
def characterize(x, c):
    i = 0
    while (i < 50):
        y = function(x, c)
        x = y
        i = i + 1
        # a the condition for instability ? this is jank
        if (x > 5 or x < -5):
            y = 123
            break
    return y

for c in c_range:
    y = characterize(0, c)
    if (y != 123):
        # more iterations :P
        i = 0
        while (i < 50):
            x = y
            y = function(x, c)
            i = i + 1
            # again, not plotting extraneous values
            if (y < 2 and y > -2):
                plt.scatter(c, y, c='black', marker='.')
            else:
                break

plt.grid()
plt.show()
