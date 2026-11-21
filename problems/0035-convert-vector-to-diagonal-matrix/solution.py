import numpy as np

def make_diagonal(x):
    n = len(x)
    diag = np.zeros((n, n))
    for i in range(n):
        diag[i][i] = x[i]
    return diag