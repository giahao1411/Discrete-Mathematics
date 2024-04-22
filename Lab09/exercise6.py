import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge(u_of_edge="A", v_of_edge="B", weight=1)
G.add_edge(u_of_edge="B", v_of_edge="D", weight=2)
G.add_edge(u_of_edge="B", v_of_edge="E", weight=3)
G.add_edge(u_of_edge="D", v_of_edge="E", weight=5)
G.add_edge(u_of_edge="A", v_of_edge="E", weight=2)
G.add_edge(u_of_edge="A", v_of_edge="C", weight=4)
G.add_edge(u_of_edge="C", v_of_edge="F", weight=6)
G.add_edge(u_of_edge="C", v_of_edge="G", weight=7)
nx.draw(G=G, with_labels=True)

plt.show()
