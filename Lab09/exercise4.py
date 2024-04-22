import networkx as nx

G = nx.Graph()

G.add_edge(u_of_edge="A", v_of_edge="B", weight=4)
G.add_edge(u_of_edge="B", v_of_edge="D", weight=2)
G.add_edge(u_of_edge="A", v_of_edge="C", weight=3)
G.add_edge(u_of_edge="C", v_of_edge="D", weight=4)
print(nx.shortest_path(G=G, source="A", target="D", weight="weight"))
