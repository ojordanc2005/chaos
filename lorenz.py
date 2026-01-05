from matplotlib import pyplot as plt
import numpy as np

# the Lorenz attractor is the soliution of 3 coupled differential equations originally proposed to model atmospheric currents

# x = 	the convective flow
# y = 	the horizontal temperature distribution
# z = 	the vertical temperature distribution

# σ = 	the ratio of viscosity to thermal conductivity
# ρ = 	the temperature difference between the top and bottom of the slice
# β = 	the width to height ratio of the slice

# dx/dt = 	σ(y − x)
# dy/dt = 	ρx − y − xz
# dz/dt = 	xy − βz

# some interesting initial conditions

sigma = 10
rho = 28
beta = 8/3

x = 0
y = 0
z = 0

# iterating over a decent timeframe

i = 0
for i in range(1000):
    dx = sigma * (y - x)
    dy = (rho * x) - y - (x * z)
    dz = (x * y) - (beta * z)

    x = x + dx
    y = y + dy
    z = z + dz

    i = i + 1

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# ax.scatter(xs, ys, zs, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
