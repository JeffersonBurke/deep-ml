import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    ones = np.arange(1, len(a)+1, 1)
    ones = ones / ones
    return np.dot(a, ones)
