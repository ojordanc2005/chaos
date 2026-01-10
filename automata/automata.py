import numpy as np
from matplotlib import pyplot as plt

# i want to program a generic cellular automata that generates to the terminal

# there are 21 bits in a "bitstring"
bitstring = np.zeros(21)
#print(bitstring)

# for now, i'll represent an uncolored bit as a zero and colored as 1

bitstring[10] = 1
#print(bitstring)

def getNeighborhood(bitstring, index):
    # edge cases
    if (index == 0):
        neighborhood = (bitstring[20], bitstring[index], bitstring[index + 1])
    elif (index == 20):
        neighborhood = (bitstring[index - 1], bitstring[index], bitstring[0])
    else:
        neighborhood = (bitstring[index - 1], bitstring[index], bitstring[index + 1])
    return neighborhood

# each bit is updated depending on the values next to it
# so, i'll iterate through each bit and update it based on
# the rules for the near bits

# for now, i have the rules integrated into this main loop,
# but i wonder if there's a better way to do this...

# this could be user configurable
n_iterations = 30

i = 0
new_bitstring = np.zeros(21)
iteration = 0

fig = plt.figure()
ax = plt.axes()
ax.set_facecolor('black')
x = [0, 1, 1, 0]
y = [n_iterations, n_iterations,
n_iterations - 1, n_iterations - 1]
ax.fill(x, y, color='black')

while (iteration < n_iterations):
    new_bitstring = np.zeros(21)

    # now i'll add some more fun rules
    for i in range(len(bitstring)):
        if (getNeighborhood(bitstring, i) == (0,0,0)):
            new_bitstring[i] = 0
            #ax.scatter(i, n_iterations - iteration, color = 'black', marker='s', s=1000)
            x = [i, i+1, i+1, i]
            y = [n_iterations - iteration, n_iterations - iteration,
                 n_iterations - iteration - 1, n_iterations - iteration - 1]
            ax.fill(x, y, color='black')
        if (getNeighborhood(bitstring, i) == (1,0,0)):
            new_bitstring[i] = 1
            #ax.scatter(i, n_iterations - iteration, color = 'black', marker='s', s=1000)
            x = [i, i+1, i+1, i]
            y = [n_iterations - iteration, n_iterations - iteration,
                 n_iterations - iteration - 1, n_iterations - iteration - 1]
            ax.fill(x, y, color='white')
        if (getNeighborhood(bitstring, i) == (0,1,0)):
            new_bitstring[i] = 0
            #ax.scatter(i, n_iterations - iteration, color = 'black', marker='s', s=1000)
            x = [i, i+1, i+1, i]
            y = [n_iterations - iteration, n_iterations - iteration,
                 n_iterations - iteration - 1, n_iterations - iteration - 1]
            ax.fill(x, y, color='black')
        if (getNeighborhood(bitstring, i) == (0,0,1)):
            new_bitstring[i] = 1
            #ax.scatter(i, n_iterations - iteration, color = 'white', marker='s', s=1000)
            x = [i, i+1, i+1, i]
            y = [n_iterations - iteration, n_iterations - iteration,
                 n_iterations - iteration - 1, n_iterations - iteration - 1]
            ax.fill(x, y, color='white')
        if (getNeighborhood(bitstring, i) == (1,1,0)):
            new_bitstring[i] = 1
            #ax.scatter(i, n_iterations - iteration, color = 'black', marker='s', s=1000)
            x = [i, i+1, i+1, i]
            y = [n_iterations - iteration, n_iterations - iteration,
                 n_iterations - iteration - 1, n_iterations - iteration - 1]
            ax.fill(x, y, color='white')
        if (getNeighborhood(bitstring, i) == (0,1,1)):
            new_bitstring[i] = 1
            #ax.scatter(i, n_iterations - iteration, color = 'black', marker='s', s=1000)
            x = [i, i+1, i+1, i]
            y = [n_iterations - iteration, n_iterations - iteration,
                 n_iterations - iteration - 1, n_iterations - iteration - 1]
            ax.fill(x, y, color='white')
        if (getNeighborhood(bitstring, i) == (1,0,1)):
            new_bitstring[i] = 0
            #ax.scatter(i, n_iterations - iteration, color = 'black', marker='s', s=1000)
            x = [i, i+1, i+1, i]
            y = [n_iterations - iteration, n_iterations - iteration,
                 n_iterations - iteration - 1, n_iterations - iteration - 1]
            ax.fill(x, y, color='black')
        if (getNeighborhood(bitstring, i) == (1,1,1)):
            new_bitstring[i] = 1
            #ax.scatter(i, n_iterations - iteration, color = 'black', marker='s', s=1000)
            x = [i, i+1, i+1, i]
            y = [n_iterations - iteration, n_iterations - iteration,
                 n_iterations - iteration - 1, n_iterations - iteration - 1]
            ax.fill(x, y, color='white')


    bitstring = new_bitstring
    iteration = iteration + 1
    print(new_bitstring)

plt.show()