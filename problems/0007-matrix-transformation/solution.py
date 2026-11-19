import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

    numA = np.array(A)
    numT = np.array(T)
    numS = np.array(S)
    detT = np.linalg.det(numT)
    detS = np.linalg.det(numS)
    if detT == 0 or detS == 0:
        return -1

    transformed_matrix = np.linalg.inv(numT) @ numA @ numS
    return transformed_matrix.tolist()