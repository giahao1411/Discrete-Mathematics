import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge(u_of_edge="0", v_of_edge="1", weight=3)
G.add_edge(u_of_edge="0", v_of_edge="3", weight=7)
G.add_edge(u_of_edge="0", v_of_edge="4", weight=8)
G.add_edge(u_of_edge="1", v_of_edge="2", weight=1)
G.add_edge(u_of_edge="1", v_of_edge="3", weight=4)
G.add_edge(u_of_edge="2", v_of_edge="3", weight=2)
G.add_edge(u_of_edge="3", v_of_edge="4", weight=3)

nx.draw(G=G, with_labels=True)
plt.show()

print(nx.shortest_path(G=G, source="1", target="4", weight="weight"))
