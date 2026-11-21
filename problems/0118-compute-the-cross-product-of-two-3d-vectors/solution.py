import numpy as np

def cross_product(a, b):
    
    z = np.zeros((3))
    z[0] = a[1]*b[2] - a[2]*b[1]
    z[1] = -(a[0]*b[2]-a[2]*b[0])
    z[2] = a[0]*b[1]-a[1]*b[0]

    return z