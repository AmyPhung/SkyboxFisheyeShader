"""
This is a demo script that shows the basic functionality behind dewarping a
fisheye projection onto normalized fisheye coordinates.
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse
from helpers import *

# Parse input arguments for modularization of code
Parser = argparse.ArgumentParser()
Parser.add_argument("-p","--polar", action="store_true",
                    help="Generate the hemisphere points at evenly spaced polar coordinates\
                     instead of cartesian coordinates")
Args = Parser.parse_args()

# Create a list of vectors
# Each vector is a 3D point on the edge of a hemisphere
pts = []
if Args.polar:
    # raise Exception("Polar not yet implemented")
    r = 1
    for theta in np.linspace(0,np.pi,20):
        for phi in np.linspace(0,np.pi,20):
            # Convert polar coordinates to cartesian coordinates
            pts.append(np.array(polarToCartesian(r,theta,phi)))

else: # Cartesian
    for x in np.linspace(-1,1,30):
        for y in np.linspace(-1,1,30):
            pts.append(np.array([x,y,calculateHemisphereZ(x,y)]))

# Convert the points into an easier data format to input to plotting functions
xs = [point[0] for point in pts]
ys = [point[1] for point in pts]
zs = [point[2] for point in pts]

# Create a 3D figure for plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d", xlim=[-4,4], ylim=[-4,4], zlim=[0,8])

# Plot our hemisphere
ax.scatter(xs, ys, zs)

# Transform the points to normalised fisheye coordinates
rs = []
for (x,y,z) in zip(xs,ys,zs):
    r = np.pi * np.arctan2(np.sqrt(x**2+y**2), z)
    rs.append(r)

phis = []
for (x,y) in zip(xs,ys):
    phis.append(np.arctan2(y,x))

xs_new = []
ys_new = []
for (r,phi) in zip(rs,phis):
    xs_new.append(r*np.cos(phi))
    ys_new.append(r*np.sin(phi))

# Plot our remapped coordinates
ax.scatter(xs_new,ys_new,0.0)

# Show the plot
plt.show()
