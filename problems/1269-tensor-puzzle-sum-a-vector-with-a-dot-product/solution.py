import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    return np.dot(np.arange(1, len(a)+1, 1) * 0 + 1, a)
