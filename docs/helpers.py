import numpy as np

def calculateHemisphereZ(x,y):
    # Center of sphere
    a = 0
    b = 0
    c = 0

    # Radius
    r = 1.0

    # Sphere equation rearranged to solve for z
    z = np.sqrt(r**2 - (x-a)**2 -(y-b)**2 )

    return z

def polarToCartesian(r, theta, phi):
    x = r*np.sin(theta)*np.cos(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(theta)
    return [x,y,z]
