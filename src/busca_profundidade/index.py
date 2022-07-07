result = []

# Realizar busca em profundidade
def dfs(visited: list[int], graph: dict[list[int]], node: int): 
    if node not in visited:
        result.append(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

    
    return result
    
print(result)