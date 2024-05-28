import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def calculateMatrix(A):
    plt.imshow(A, cmap="Blues", interpolation="none")
    plt.colorbar()
    plt.xticks(np.arange(len(A)))
    plt.yticks(np.arange(len(A)))
    plt.xlabel("Nodes")
    plt.ylabel("Nodes")
    plt.title("Weighted Matrix")
    plt.show()


def plotMatrix(A, enumerates):
    G = nx.from_numpy_array(A)
    pos = nx.spring_layout(G)
    nx.draw_networkx(
        G, pos=pos, with_labels=True, labels={a: b for a, b in enumerate(enumerates)}
    )
    nx.draw_networkx_edge_labels(G, font_size=6, pos=pos, label_pos=0.5)
    plt.axis("equal")
    plt.show()


# test cases for calculate and plot matrices
A = np.array(
    [
        [0, 0, 3, 0, 1],
        [0, 0, 5, 3, 0],
        [3, 5, 0, 1, 0],
        [0, 3, 1, 0, 2],
        [1, 0, 0, 2, 0],
    ]
)

B = np.array(
    [
        [0, 0, 0, 0, 1, 1],
        [0, 0, 5, 3, 0, 0],
        [0, 5, 0, 1, 5, 0],
        [0, 3, 1, 0, 2, 3],
        [1, 0, 5, 2, 0, 6],
        [1, 0, 0, 3, 6, 0],
    ]
)

calculateMatrix(A)
plotMatrix(A, "abcde")

calculateMatrix(B)
plotMatrix(B, "abcdef")
