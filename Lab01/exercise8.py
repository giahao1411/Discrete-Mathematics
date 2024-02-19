# exercise 8


# Hint: the product of matrix A size m × n and B size n × q is matrix C size m × q
def mProd(A, B):
    # check if the matrices have the same dimensions
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimension error")

    # determine the dimensions of the matrices
    rowsA = len(A)
    colsA = len(A[0])
    colsB = len(B[0])

    # create an empty result matrix
    C = [[0] * colsB for _ in range(rowsA)]

    # loop to calculate the product of 2 matrices
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                C[i][j] += A[i][k] * B[k][j]

    return C


A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]

result = mProd(A, B)
print(result)
