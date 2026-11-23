import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    dim = arr.ndim
    if norm_type == "l1":
        sum = 0
        if dim == 1:
            for i in range(len(arr)):
                sum += abs(arr[i])
            return sum
        else:
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    sum += abs(arr[i][j])
            return sum
    elif norm_type == "l2":
        sum = 0
        if dim == 1:
            for i in range(len(arr)):
                sum += arr[i] ** 2
            return sum ** (1/2)
        else:
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    sum += arr[i][j] ** 2
            return sum ** (1/2)
    elif norm_type == "linf":
        if dim == 1:
            max = abs(arr[0])
            for i in range(len(arr)):
                if abs(arr[i]) > max:
                    max = abs(arr[i])
            return max
        else:
            max = abs(arr[0][0])
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    if abs(arr[i][j]) > max:
                        max = abs(arr[i][j])
            return max
    elif norm_type == "frobenius":
        if dim == 1:
            raise ValueError("Array must be 2d")
        else:
            sum = 0
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    sum += arr[i][j] ** 2
            return sum ** (1/2)
    else:
        return None         
