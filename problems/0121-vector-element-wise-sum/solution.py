def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
    # Return the element-wise sum of vectors 'a' and 'b'.
    # If vectors have different lengths, return -1.

    n = len(a)
    if n != len(b):
        return -1
    
    z = []
    for i in range(n):
        z.append(a[i] + b[i])

    return z