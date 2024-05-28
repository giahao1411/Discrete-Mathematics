import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# add nodes
G.add_nodes_from(
    [
        "Multicellular organisms",
        "Animals",
        "Mammals",
        "Unicellular organisms",
    ]
)

G.add_edges_from(
    [
        ("Mammals", "Primates"),
        ("Mammals", "Rodents"),
        ("Animals", "Mammals"),
        ("Animals", "Reptiles"),
        ("Multicellular organisms", "Animals"),
        ("Multicellular organisms", "Plants"),
        ("Multicellular organisms", "Fungi"),
        ("Unicellular organisms", "Yeasts"),
    ]
)

# draw the graph
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_size=1000, font_size=7)

plt.title("Relationships of Terms")
plt.axis("off")
plt.show()
