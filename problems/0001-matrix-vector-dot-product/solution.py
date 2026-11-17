def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    result = []
    if (len(a) != len(a[0])):
        return -1

    for i in range(len(a)):
        sum = 0
        for j in range(len(a[0])):
            sum += a[i][j] * b[j]
        result.append(sum)

    return result