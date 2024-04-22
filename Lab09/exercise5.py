import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from(ebunch_to_add=[("1", "4"), ("4", "2"), ("3", "4")])
nx.draw(G=G, with_labels=True)
plt.show()
