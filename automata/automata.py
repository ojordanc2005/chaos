import numpy as np
from matplotlib import pyplot as plt

# i want to program a generic cellular automata that generates to the terminal

# this must be even, for now
n_iterations = 300

# doing away with the idea of bitstrings...
bitstring = np.zeros(2*(n_iterations + 1))
bitstring = np.random.randint(0,2,2*(n_iterations + 1))
bitstring = np.ones(2*(n_iterations + 1))


# i'll represent an uncolored bit as a zero and colored as 1
center_index = int(n_iterations + 1)
bitstring[center_index] = 1
bitstring[center_index] = 0

#print(bitstring)

def getNeighborhood(bitstring, index, iteration):
    # edge cases

    #if (index == center_index - iteration - 1):
    #    neighborhood = (bitstring[center_index + iteration - 1], bitstring[center_index + iteration], bitstring[index + 1])

    #elif (index == center_index + iteration + 1):
    #    neighborhood = (bitstring[index - 1], bitstring[center_index - iteration], bitstring[center_index - iteration + 1])

    if (index == center_index - iteration):
        neighborhood = (bitstring[center_index + iteration], bitstring[index], bitstring[index + 1])

    elif (index == center_index + iteration):
        neighborhood = (bitstring[index - 1], bitstring[index], bitstring[center_index - iteration])

    elif (index == len(bitstring) - 1):
        neighborhood = (bitstring[index - 1], bitstring[index], bitstring[0])

    else:
        neighborhood = (bitstring[index - 1], bitstring[index], bitstring[index + 1])

    return neighborhood

i = 0
new_bitstring = np.zeros(2*(n_iterations + 1))
iteration = 0

fig = plt.figure()
ax = plt.axes()
ax.set_facecolor('black')
#ax.set_xlim(0, n_iterations)
#ax.set_ylim(0, n_iterations + 1)


x = [center_index, center_index + 1, center_index + 1, center_index]
y = [n_iterations, n_iterations,
n_iterations - 1, n_iterations - 1]
ax.fill(x, y, color='white')

def plot(i, color):
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
#for iteration in range(n_iterations):
    new_bitstring = np.zeros(2*(n_iterations + 1))
    iteration = iteration + 1
    # now i'll add some more fun rules
    for i in range(len(bitstring)):
        if (getNeighborhood(bitstring, i, iteration) == (0,0,0)):
            new_bitstring[i] = 1

        if (getNeighborhood(bitstring, i, iteration) == (1,0,0)):
            new_bitstring[i] = 0

        if (getNeighborhood(bitstring, i, iteration) == (0,1,0)):
            new_bitstring[i] = 1

        if (getNeighborhood(bitstring, i, iteration) == (0,0,1)):
            new_bitstring[i] = 0

        if (getNeighborhood(bitstring, i, iteration) == (1,1,0)):
            new_bitstring[i] = 1

        if (getNeighborhood(bitstring, i, iteration) == (0,1,1)):
            new_bitstring[i] = 1

        if (getNeighborhood(bitstring, i, iteration) == (1,0,1)):
            new_bitstring[i] = 1

        if (getNeighborhood(bitstring, i, iteration) == (1,1,1)):
            new_bitstring[i] = 0
            
        plot(i, new_bitstring[i])
        #print(center_index - iteration)

    bitstring = new_bitstring
    #iteration = iteration + 1
    #print(iteration)
    print(f"iteration: {iteration}")
    print(new_bitstring)

save = True
#save = False
if (save == True):
    plt.savefig("./rule_73/single_300.png")

plt.show() 