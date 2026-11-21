import numpy as np

def calculate_dot_product(vec1, vec2):
    sum = 0
    for i in range(len(vec1)):
        sum += vec1[i] * vec2[i]
    return sum