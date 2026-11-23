import numpy as np

def cosine_similarity(v1, v2):

    normv1 = 0
    normv2 = 0
    dot = 0
    for i in range(len(v1)):
        normv1 += v1[i] ** 2
        normv2 += v2[i] ** 2
        dot += v1[i] * v2[i]
    normv1 = normv1 ** (1/2)
    normv2 = normv2 ** (1/2)

    return dot / (normv1 * normv2)