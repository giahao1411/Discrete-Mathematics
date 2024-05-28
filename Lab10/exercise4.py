import numpy as np


def toLoE(A):
    edges = []
    nodes_name = ["A", "B", "C", "D", "E", "F"]
    num_nodes = A.shape[0]

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = A[i, j]
            if weight != 0:
                edges.append((nodes_name[i], nodes_name[j], weight))

    return edges


A = np.array(
    [
        [0, 0, 5, 3, 0, 0],
        [0, 0, 3, 2, 0, 0],
        [5, 3, 0, 1, 3, 0],
        [3, 2, 1, 0, 1, 3],
        [0, 0, 3, 1, 0, 4],
        [0, 0, 0, 3, 4, 0],
    ]
)

B = np.array(
    [
        [0, 0, 2, 3, 3, 0],
        [0, 0, 3, 2, 0, 0],
        [2, 3, 0, 2, 8, 6],
        [3, 2, 2, 0, 0, 5],
        [3, 0, 8, 0, 0, 3],
        [0, 0, 6, 5, 3, 0],
    ]
)

print(toLoE(A))
print(toLoE(B))
