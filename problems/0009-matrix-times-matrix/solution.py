def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    n = len(a)
    m = len(a[0])
    l = len(b)
    p = len(b[0])
    if m != l:
        return -1
    
    c = []

    for i in range(n):
        row = []
        for j in range(p):
            sum = 0
            for k in range(m):
                sum += a[i][k] * b[k][j]
            row.append(sum)
        c.append(row)

    
    return c