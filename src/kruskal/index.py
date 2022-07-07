# Algoritmo de Kruskal

class Graph:
    def __init__(self, vertices):
        self.num_vertices: int = vertices
        self.graph: list[list[int]] = []    # [[0, 1, 4], [0, 2, 4], ...]

    def add_edge(self, node_1: int, node_2: int, weight: int):
        self.graph.append([node_1, node_2, weight])

    # Search function

    def find(self, parent: list[int], index: int):
        if parent[index] == index:
            return index

        return self.find(parent, parent[index])

    def apply_union(self, parent, rank, node_x, node_y):
        node_x_root = self.find(parent, node_x)
        node_y_root = self.find(parent, node_y)

        if rank[node_x_root] < rank[node_y_root]:
            parent[node_x_root] = node_y_root
        elif rank[node_x_root] > rank[node_y_root]:
            parent[node_y_root] = node_x_root
        else:
            parent[node_y_root] = node_x_root
            rank[node_x_root] += 1

    #  Executando algoritmo de Kruskal
    def kruskal_algo(self):
        result = []
        parent = []
        rank = []
        index, count = 0, 0

        # Ordena o grafo de acordo com o weight (menor weight para maior weight)
        self.graph = sorted(self.graph, key=lambda item: item[2])

        for node in range(self.num_vertices):
            parent.append(node)     # parent =  [0, 1, 2, 3, 4, 5]
            rank.append(0)          # rank =    [0, 0, 0, 0, 0, 0]

        while count < self.num_vertices - 1:
            node_1, node_2, weight = self.graph[index]
            index = index + 1
            x = self.find(parent, node_1)
            y = self.find(parent, node_2)
            if x != y:
                count += 1
                result.append([node_1, node_2, weight])
                self.apply_union(parent, rank, x, y)

        for node_1, node_2, weight in result:
            print(f"{node_1} - {node_2}: {weight}")
        
        return result


""" g = Graph(6)            # grafo de 6 vértices [0, .., 5]

g.add_edge(0, 1, 4)     # add aresta nos vértices 0 e 1 de valor 4
g.add_edge(0, 2, 4)     # add aresta nos vértices 0 e 2 de valor 4
g.add_edge(1, 2, 2)     # ...
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)

g.kruskal_algo()        # Executar algoritmo de kruskal """