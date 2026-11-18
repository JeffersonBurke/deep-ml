def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    n = len(a)
    m = len(a[0])
    at = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(a[j][i])
        at.append(row)
    return at
