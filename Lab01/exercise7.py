# exercise 7


def mSum(A, B):
    # check if the matrices have the same dimensions/atrix size
    if (len(A) != len(B)) or (len(A[0]) != len(B[0])):
        raise ValueError("Matrix dimension error")

    # create a result matrix that have the same dimension
    C = [[0] * len(A[0]) for _ in range(len(A))]

    # loop to sum
    for i in range(len(A)):
        for j in range(len(B)):
            C[i][j] = A[i][j] + B[i][j]

    return C


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = mSum(A, B)
print(result)
