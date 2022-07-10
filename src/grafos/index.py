from kruskal.index import Graph

def get_graph_1():
    graph_1 = Graph(6)            # Cria grafo de 6 vértices

    graph_1.add_edge(0, 1, 4)     # add aresta nos vértices 0 e 1 de valor 4
    graph_1.add_edge(0, 2, 4)     # add aresta nos vértices 0 e 2 de valor 4
    graph_1.add_edge(1, 2, 2)     # ...
    graph_1.add_edge(1, 0, 4)
    graph_1.add_edge(2, 0, 4)
    graph_1.add_edge(2, 1, 2)
    graph_1.add_edge(2, 3, 3)
    graph_1.add_edge(2, 5, 2)
    graph_1.add_edge(2, 4, 4)
    graph_1.add_edge(3, 2, 3)
    graph_1.add_edge(3, 4, 3)
    graph_1.add_edge(4, 2, 4)
    graph_1.add_edge(4, 3, 3)
    graph_1.add_edge(5, 2, 2)
    graph_1.add_edge(5, 4, 3)

    return graph_1

def get_graph_2():
    graph_2 = Graph(9)            # Cria grafo de 9 vértices

    graph_2.add_edge(0, 1, 48)     
    graph_2.add_edge(0, 8, 32)     
    graph_2.add_edge(1, 0, 48)     
    graph_2.add_edge(1, 2, 30)     
    graph_2.add_edge(1, 7, 15)
    graph_2.add_edge(2, 7, 24)
    graph_2.add_edge(2, 3, 22)
    graph_2.add_edge(2, 1, 30)
    graph_2.add_edge(3, 4, 9)
    graph_2.add_edge(3, 7, 31)
    graph_2.add_edge(3, 2, 22)
    graph_2.add_edge(4, 5, 12)
    graph_2.add_edge(4, 6, 4)
    graph_2.add_edge(4, 3, 9)
    graph_2.add_edge(5, 4, 12)
    graph_2.add_edge(5, 6, 6)
    graph_2.add_edge(5, 8, 8)
    graph_2.add_edge(6, 7, 15)
    graph_2.add_edge(6, 4, 4)
    graph_2.add_edge(6, 5, 6)
    graph_2.add_edge(7, 8, 15)
    graph_2.add_edge(7, 3, 31)
    graph_2.add_edge(7, 2, 24)
    graph_2.add_edge(7, 1, 15)
    graph_2.add_edge(7, 6, 15)
    graph_2.add_edge(8, 0, 32)
    graph_2.add_edge(8, 5, 8)
    graph_2.add_edge(8, 7, 15)

    return graph_2
