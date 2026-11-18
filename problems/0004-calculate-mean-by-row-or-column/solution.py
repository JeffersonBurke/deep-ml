def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    n = len(matrix)
    m = len(matrix[0])
    if mode == 'row':
        for i in range(n):
            sum = 0
            for j in range(m):
                sum += matrix[i][j]
            means.append(sum/m)
        return means

    elif mode == 'column':
        for j in range(m):
            sum = 0
            for i in range(n):
                sum += matrix[i][j]
            means.append(sum/n)
        return means

    else:
        return 0