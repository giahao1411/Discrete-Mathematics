import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge("0", "1", weight=0.54)
G.add_edge("0", "2", weight=0.14)
G.add_edge("0", "7", weight=0.47)
G.add_edge("1", "2", weight=0.63)
G.add_edge("1", "3", weight=0.35)
G.add_edge("1", "4", weight=0.30)
G.add_edge("1", "7", weight=0.31)
G.add_edge("2", "3", weight=0.31)
G.add_edge("3", "4", weight=0.54)
G.add_edge("3", "5", weight=0.43)
G.add_edge("3", "7", weight=0.13)
G.add_edge("4", "5", weight=0.54)
G.add_edge("4", "6", weight=0.62)
G.add_edge("4", "7", weight=0.54)
G.add_edge("5", "6", weight=0.37)

nx.draw(G=G, with_labels=True)
plt.show()

print(nx.shortest_path(G=G, source="0", target="6", weight="weight"))
