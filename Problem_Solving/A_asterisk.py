# A* Search

import heapq

graph = { 
    'A': [('B', 1), ('C', 3)], 
    'B': [('D', 3), ('E', 1)], 
    'C': [('F', 5)], 
    'D': [], 
    'E': [('F', 2)], 
    'F': [] 
}

heuristic = {
    'A': 4,
    'B': 2,
    'C': 4,
    'D': 4,
    'E': 1,
    'F': 0
}

def a_star(graph, start, goal):
    pq = [(heuristic[start], 0, start, [])]
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)
        
        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == goal:
            return path, g
        
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(pq, (f_new, g_new, neighbor, path))
        return None, float('inf')
    
path, cost = a_star(graph, 'A', 'F')
print("Path: ", path)
print("Cost: ", cost)

# A* Search
# A* Search uses:
# f(n) = g(n) + h(n)
# where:
#   g(n) = actual path cost from start node
#   h(n) = heuristic estimate to goal