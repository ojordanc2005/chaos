from matplotlib import pyplot as plt
import numpy as np

# fun bifurcation mapping code! define a function, the code will ask for you to choose a seed,
# c value, and number of iterations.

# a fun one is x^2 + c, 0, c=-1.8, and 1000

# these are known as cobweb plots

# the definition of iteration
x_range = np.linspace(-2,2,40)
y = x_range
plt.plot(x_range, y)

def function(x, c):
    y = x**2 + c
    return y

seed = float(input("Choose a seed: "))
c = float(input("Choose a c value: "))
n_iterations = int(input("How many iterations do you want to see?: "))

y_range = function(x_range, c)

plt.plot(x_range,y_range)
plt.grid()
#plt.show(block=False)

# x needs to be a param
'''def iterateAndDraw(x, c):
    up = True

    if x>function(x, c):
        up = False

    if (up is True):
        plt.vlines(x = x, ymin = function(x, c), ymax= x)
    else:
        plt.vlines(x = x, ymin = x, ymax= function(x, c))

    return x'''

x = seed
up = True
right = True
i = 0
for i in range(n_iterations):
    if i % 2 != 0:
        # iterate horizontally
        if x < function(x, c):
            right = False
        if (right is True):
            plt.hlines(y = function(x, c), xmin = function(x, c), xmax= x)
        else:
            plt.hlines(y = function(x, c), xmin = x, xmax= function(x, c))
        x = function(x, c)
    else:
        #iterate vertically
        if x > function(x, c):
            up = False
        if (up is True):
            plt.vlines(x = x, ymin = function(x, c), ymax= x)
        else:
            plt.vlines(x = x, ymin = x, ymax= function(x, c))

#iterateAndDraw(seed, c)
#plt.show(block=False)
plt.show()

'''
# I want to make this code pretty interactive
whatToDo = input("What next? (stop or iterate): ")
print(whatToDo)

if(whatToDo == "iterate"):
    #something else
    print('hi')

elif(whatToDo == "stop"):
    exit()'''
