import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge("v1", "v2", weight=5)
G.add_edge("v1", "v3", weight=6)
G.add_edge("v2", "v3", weight=8)
G.add_edge("v2", "v4", weight=3)
G.add_edge("v2", "v5", weight=4)
G.add_edge("v3", "v5", weight=6)
G.add_edge("v4", "v5", weight=3)
G.add_edge("v4", "v6", weight=7)
G.add_edge("v5", "v6", weight=7)

nx.draw(G=G, with_labels=True)
plt.show()

print(nx.shortest_path(G=G, source="v1", target="v6", weight="weight"))