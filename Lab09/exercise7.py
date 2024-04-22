import networkx as nx

G = nx.Graph()

G.add_edge("A", "B", weight=1)
G.add_edge("B", "D", weight=2)
G.add_edge("B", "E", weight=3)
G.add_edge("D", "E", weight=5)
G.add_edge("A", "E", weight=2)
G.add_edge("A", "C", weight=4)
G.add_edge("C", "F", weight=6)
G.add_edge("C", "G", weight=7)
print(nx.shortest_path(G, "A", "D", weight="weight"))
