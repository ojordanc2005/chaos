import numpy as np
from matplotlib import pyplot as plt

# i want to program a generic cellular automata that generates to the terminal

# there are 21 bits in a "bitstring"
bitstring = np.zeros(21)

# i'll represent an uncolored bit as a zero and colored as 1
bitstring[10] = 1

def getNeighborhood(bitstring, index):
    # edge cases
    if (index == 0):
        neighborhood = (bitstring[20], bitstring[index], bitstring[index + 1])
    elif (index == 20):
        neighborhood = (bitstring[index - 1], bitstring[index], bitstring[0])
    else:
        neighborhood = (bitstring[index - 1], bitstring[index], bitstring[index + 1])
    return neighborhood

# this could be user configurable
n_iterations = 60

i = 0
new_bitstring = np.zeros(21)
iteration = 0

fig = plt.figure()
ax = plt.axes()
ax.set_facecolor('black')
ax.set_xlim(0, n_iterations)

x = [10, 11, 11, 10]
y = [n_iterations + 1, n_iterations + 1,
n_iterations, n_iterations]
ax.fill(x, y, color='white')

def plot(index, color):
    if (color == 1):
        x = [i, i+1, i+1, i]
        y = [n_iterations - iteration, n_iterations - iteration,
             n_iterations - iteration - 1, n_iterations - iteration - 1]
        ax.fill(x, y, color='white')
    else:
        x = [i, i+1, i+1, i]
        y = [n_iterations - iteration, n_iterations - iteration,
             n_iterations - iteration - 1, n_iterations - iteration - 1]
        ax.fill(x, y, color='black')

# main loop
while (iteration < n_iterations):
    new_bitstring = np.zeros(21)

    # now i'll add some more fun rules
    for i in range(len(bitstring)):
        if (getNeighborhood(bitstring, i) == (0,0,0)):
            new_bitstring[i] = 0

        if (getNeighborhood(bitstring, i) == (1,0,0)):
            new_bitstring[i] = 1

        if (getNeighborhood(bitstring, i) == (0,1,0)):
            new_bitstring[i] = 1

        if (getNeighborhood(bitstring, i) == (0,0,1)):
            new_bitstring[i] = 1

        if (getNeighborhood(bitstring, i) == (1,1,0)):
            new_bitstring[i] = 0

        if (getNeighborhood(bitstring, i) == (0,1,1)):
            new_bitstring[i] = 1

        if (getNeighborhood(bitstring, i) == (1,0,1)):
            new_bitstring[i] = 0

        if (getNeighborhood(bitstring, i) == (1,1,1)):
            new_bitstring[i] = 0
            
        plot(i, new_bitstring[i])

    bitstring = new_bitstring
    iteration = iteration + 1
    print(new_bitstring)

save = True
if (save == True):
    plt.savefig("rule_30.png")

plt.show()