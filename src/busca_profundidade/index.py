result = []
count = 0

def increment():
    global count
    count += 1

def reset():
    global count
    count = 0
    result.clear()

# Realizar busca em profundidade
def dfs(limit: int, graph: 'dict[list[int]]', node: int, first_time: bool = False): 
    if first_time:
        reset()

    increment()

    if count >= limit: 
        return result

    result.append(node)
    
    for neighbour in graph[node]:
        dfs(limit, graph, neighbour)
    return result

    