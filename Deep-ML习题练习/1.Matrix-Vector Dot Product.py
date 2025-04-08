#题目描述
#Write a Python function that computes the dot product of a matrix and a vector. 
# The function should return a list representing the resulting vector if the operation is valid, 
# or -1 if the matrix and vector dimensions are incompatible. 
# A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector.
#  For example, an n x m matrix requires a vector of length m.

#solution
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if len(a[0]) != len(b):
        return -1
    result = []
    for row in a:
        total = 0
        for i in range(len(row)):
            total += row[i] * b[i]
        result.append(total)
    return result