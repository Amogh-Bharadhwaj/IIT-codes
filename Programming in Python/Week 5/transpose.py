'''Write a function named transpose that accepts a matrix mat as input and returns its transpose.'''4

def transpose(mat):
    result =[[0 for i in range(len(mat))] for j in range(len(mat[0]))]
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            result[c][r] = mat[r][c]
    return result