from matplotlib import pyplot as plt
import numpy as np

# the Julia set extends the quadratic mapping that we explored previously
# to the complex plane.

# in Python, it's pretty easy to work with complex numbers

'''
z0 = 1 + 2j
z1 = 2 + 1j

print(z0, z1)
print (z0.real)
print(z1.imag)

print(z0*z0 + z1)'''

# what I think of when I think of the Julia set occurs when c = (-3/4, 0). 
# another interesting one is at c = (−0.500, +0.563)
# also try c is approximately -0.5125 + 0.5213i

c = -0.75 + 0j

# not really sure what I'm doing, but let's consider all x and y in a range

x_range = np.linspace(-4,4,10)
y_range = np.linspace(-4,4,10)

# the function
def complex_function(x, y, c):
    z = x + y*1j
    z = z**2 + c
    return z

# again we need a characterizing function
# this just iterates over the map for a given point a bunch
def characterize(x, y, c):
    i = 0
    while (i < 5):
        z = complex_function(x, y, c)
        x = z.real
        y = z.imag
        # here we need a bit more clever of a characterization scheme
        '''if (z > 100 or z < -100):
            z = 100
            break'''
        print(z)
    return z

# more iterating and plotting here
for x in x_range:
    for y in y_range:
        z = characterize(x, y, c)
        if (z != 100):
            i = 0
            while (i < 10):
                i = i + 1
                # plot 10 points for a given x and y
                z = complex_function(x, y, c)
                x = z.real
                y = z.imag

                z_mag = np.sqrt(z.real**2 + z.imag**2)
                plt.scatter(x, y, c=z_mag, cmap="summer")

                plt.colorbar(orientation="vertical")  
                plt.xlabel("Re[z]")  
                plt.ylabel("Im[z]")   
                print(x,y,z)
                                
plt.show()

# plotting...
'''
p = [100, 200, 150, 23, 30, 50, 156, 32, 67, 89]  # x
l = [50, 70, 100, 10, 10, 34, 56, 18, 35, 45]  # y  
r = [1, 0.53, 2, 0.76, 0.5, 2.125, 0.56, 1.28, 1.09, 1.02]  # z

# scatterplot
plt.scatter(p, l, c=r, cmap="summer")

# add Colorbar
plt.colorbar(orientation="vertical")  
plt.xlabel("Real")  
plt.ylabel("Imaginary")   
plt.show()
'''
