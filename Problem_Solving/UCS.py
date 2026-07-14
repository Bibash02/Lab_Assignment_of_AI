# Uniform Cost Search (UCS)

import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [],
    'F': []
}

def uniform_cost_search(graph, start, goal):
    pq = [(0, start, [])] # (cost, node, path)
    visited = set()
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)

        path = path + [node]
        if node == goal:
            return path, cost
        
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path))
    return None, float('inf')

path, cost = uniform_cost_search(graph, 'A', 'F')
print("Path:", path)
print("Cost:", cost)

# Uniform Cost Search
# Uniform Cost Search expands the node with the lowest path cost first. It is used when edges have different costs.