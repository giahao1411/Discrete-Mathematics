import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edges_from(
    ebunch_to_add=[
        ("A", "B"),
        ("A", "C"),
        ("D", "B"),
        ("E", "C"),
        ("E", "F"),
        ("B", "H"),
        ("B", "G"),
        ("B", "F"),
        ("C", "G"),
    ]
)

nx.draw(G=G)

plt.show()
