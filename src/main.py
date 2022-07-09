from kruskal.index import Graph
from convert_graph_data_type import convert
from busca_largura.index import bfs
from busca_profundidade.index import dfs
from menu import menu

def main():
    graph = Graph(6)            # Cria grafo de 6 vértices

    graph.add_edge(0, 1, 4)     # add aresta nos vértices 0 e 1 de valor 4
    graph.add_edge(0, 2, 4)     # add aresta nos vértices 0 e 2 de valor 4
    graph.add_edge(1, 2, 2)     # ...
    graph.add_edge(1, 0, 4)
    graph.add_edge(2, 0, 4)
    graph.add_edge(2, 1, 2)
    graph.add_edge(2, 3, 3)
    graph.add_edge(2, 5, 2)
    graph.add_edge(2, 4, 4)
    graph.add_edge(3, 2, 3)
    graph.add_edge(3, 4, 3)
    graph.add_edge(4, 2, 4)
    graph.add_edge(4, 3, 3)
    graph.add_edge(5, 2, 2)
    graph.add_edge(5, 4, 3)
    
    limit = 50      # limite de até quantos nós as buscas podem percorrer

    menu(graph, limit)

if __name__ == '__main__':
    main()