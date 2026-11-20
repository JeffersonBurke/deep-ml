import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:

    A = np.array(X)
    b = np.array(y)

    return np.round(np.linalg.inv(A.T @ A) @ A.T @ b, 4).tolist()