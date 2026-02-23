import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML, display

# randomizer...
#for i in range(16):
#    print(np.random.randint(1,5))

# to animate anything, you need the basic structure of a plotting function to be called and
# an animate function.

# my ax
fig = plt.figure()
ax = plt.axes()
ax.set_facecolor('black')
ax.grid()

num_walks = 30
ax.set_xlim(-num_walks/2 + 1, num_walks/2 + 1)
ax.set_ylim(-num_walks/2 + 1, num_walks/2 + 1)

ax.set_xticks((2, 3))
ax.set_yticks((2, 3))

plt.show()


# starting cube is at (0,0)
# evolution is based on number generation: 1, 2, 3, 4 -> N, E, S, W
# i'll use a grid structure to fill in squares, starting from the ordered (x,y) and extending positively

#main loop
x = 0
y = 0
move = np.random.randint(1,5)
if (move == 1):
    # move North
    y = y + 1
if (move == 2):
    # move East
    x = x + 1
if (move == 3):
    # move South
    y = y - 1
if (move == 4):
    # move West
    x = x - 1


'''
        x = [i, i+1, i+1, i]
        y = [n_iterations - iteration, n_iterations - iteration,
             n_iterations - iteration - 1, n_iterations - iteration - 1]
        ax.fill(x, y, color='white')
'''