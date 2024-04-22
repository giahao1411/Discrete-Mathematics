import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge("0", "1", weight=4)
G.add_edge("0", "7", weight=8)
G.add_edge("1", "2", weight=8)
G.add_edge("1", "7", weight=11)
G.add_edge("2", "3", weight=7)
G.add_edge("2", "8", weight=2)
G.add_edge("2", "5", weight=4)
G.add_edge("3", "4", weight=9)
G.add_edge("3", "5", weight=14)
G.add_edge("4", "5", weight=10)
G.add_edge("5", "6", weight=2)
G.add_edge("6", "7", weight=1)
G.add_edge("6", "8", weight=6)
G.add_edge("7", "8", weight=7)

nx.draw(G=G, with_labels=True)
plt.show()

print(nx.shortest_path(G=G, source="1", target="5", weight="weight"))
