# Depth First Search program:

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end = " ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

print("DFS Traversal:")
dfs('A')

# Depth First Search(DFS)
# Depth First Search explores one branch completely before moving to another branch. It uses recursion or stack.