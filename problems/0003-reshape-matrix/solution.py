import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    b = np.array(a)
    b = b.flatten()
    row = new_shape[0]
    col = new_shape[1]
    n = len(a)
    m = len(a[0])
    if (row * col != n * m):
        return []

    reshaped = np.zeros((row, col))
    count = 0
    for i in range(row):
        for j in range(col):
            reshaped[i][j] = b[count]
            count += 1
    return reshaped