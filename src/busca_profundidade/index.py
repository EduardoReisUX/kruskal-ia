result = []
count = 0

def increment():
    global count
    count += 1

# Realizar busca em profundidade
def dfs(limit: int, graph: dict[list[int]], node: int): 
    increment()
    if count >= limit: 
        return result

    result.append(node)
    
    for neighbour in graph[node]:
        dfs(limit, graph, neighbour)
    return result

    