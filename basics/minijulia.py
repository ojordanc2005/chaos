from matplotlib import pyplot as plt
import numpy as np

c = -0.75 + 0j
#c = 0 + 0j

x_range = np.linspace(-1.5,1.5,100)
y_range = np.linspace(-1.5,1.5,100)

# the function
def complex_function(x, y, c):
    z = x + y*1j
    z = z**2 + c
    return z


#it takes about 3 iterations to blow up to infinity...

# a few iterations at a few points
'''j = 0
for x in x_range:
    for y in y_range:
        i = 1
        print(x, y)
        xtemp = x
        ytemp = y
        while i < 4:
            j = j + 1
            z = complex_function(x, y, c)
            print(f'{j}: iteration number: {i} for point: {x}, {y} yields z = {z}')
            x = z.real
            y = z.imag
            print(z)
            print(x, y)
            i = i + 1
        x = xtemp
        y = ytemp'''


def characterize(x, y, c):
    i = 0
    while i < 10:
            #j = j + 1
            z = complex_function(x, y, c)
            #print(f'{j}: iteration number: {i} for point: {x}, {y} yields z = {z}')
            x = z.real
            y = z.imag
            #print(z)
            #print(x, y)
            i = i + 1
            if (z > 300 or z < -300):
                z = 100
                break
    return z

# main loop
j = 0
for x in x_range:
    for y in y_range:
        z = characterize(x, y, c)
        if (z != 100):
            i = 1
            #print(x, y)
            xtemp = x
            ytemp = y
            while i < 10:
                j = j + 1
                z = complex_function(x, y, c)
                #print(f'{j}: iteration number: {i} for point: {x}, {y} yields z = {z}')
                x = z.real
                y = z.imag
                #print(z)
                #print(x, y)
                i = i + 1
                if (z < 100 and z > -100):
                    z_mag = np.sqrt(z.real**2 + z.imag**2)
                    plt.scatter(xtemp, ytemp, c=z_mag, cmap="magma") 
            x = xtemp
            y = ytemp


plt.colorbar(orientation="vertical")  
plt.xlabel("Re[z]")  
plt.ylabel("Im[z]")  
plt.show()