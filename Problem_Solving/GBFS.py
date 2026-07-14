# Greedy Best First Search

import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# heuristic values
heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 6,
    'F': 0
}

def greedy_best_first_search(start, goal):
    pq = [(heuristic[start], start, [])]

    visited = set()

    while pq:
        h, node, path = heapq.heappop(pq)
        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == goal:
            return path
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor, path))
        return None

path = greedy_best_first_search('A', 'F')
print("Path found: ", path)


# Greedy Best First Search
# Greedy Best First Search chooses the node with the lowest heuristic value. It uses only heuristic information.