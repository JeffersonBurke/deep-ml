def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    trace = a + d
    det = a * d - b * c

    lambda1 = ((trace ** 2 - 4 * det) ** (1/2) - (-trace)) / 2
    lambda2 = (-(trace ** 2 - 4 * det) ** (1/2) - (-trace)) / 2
    eigenvalues = [lambda1, lambda2]
    return eigenvalues