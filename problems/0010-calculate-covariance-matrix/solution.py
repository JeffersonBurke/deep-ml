def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    rows = len(vectors)
    cols = len(vectors[0])
    n = rows
    means = []

    for i in range(rows):
        sum = 0
        for j in range(cols):
            sum += vectors[i][j]
        means.append(sum/cols)

    devs_from_mean = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(vectors[i][j]-means[i])
        devs_from_mean.append(row)
    
    cov = []
    for i in range(rows):
        row = []
        for z in range(rows):
            sum = 0
            for j in range(rows):
                sum += devs_from_mean[i][j] * devs_from_mean[z][j]
            if n == 1:
                row.append(sum/n)
            else:
                row.append(sum/(n-1))
        cov.append(row)
    return cov
