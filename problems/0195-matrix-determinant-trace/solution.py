def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    def helper(matrix, n):
        det = 0
        if n == 2:
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[1][0]
            d = matrix[1][1]
            det += a * d - b * c
        else:
            for i in range(n):
                new_matrix = []
                for j in range(n):
                    row = []
                    for k in range(n):
                        if (j != 0 and k != i):
                            row.append(matrix[j][k])
                    if (len(row) != 0):
                        new_matrix.append(row)
                if i % 2 == 0:
                    print(new_matrix)
                    det += matrix[0][i] * helper(new_matrix, n-1)
                else:
                    det += -1 * matrix[0][i] * helper(new_matrix, n-1)
                    print(new_matrix)

        return det
    n = len(matrix)
    trace = 0
    det = helper(matrix, n)

    for i in range(n):
        trace += matrix[i][i]
    
    tup = (det, trace)                


    return tup