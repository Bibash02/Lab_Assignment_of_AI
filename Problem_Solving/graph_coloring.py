COLORS = ["Red", "Green", "Blue", "Yellow"]

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

V = 4

def is_safe(v, graph, color, c):
    for i in range(V):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, v):
    if v == V:
        return True
    
    for c in range(1, m + 1):
        if is_safe(v, graph, color, c):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True
            color[v] = 0
    return False

def graph_coloring(graph, m):
    color = [0] * V

    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist")
        return False
    
    print("Assigned Color: ")
    for i in range(V):
        print(f"Vertex {i} --> {COLORS[color[i]-1]}")
    return True

graph_coloring(graph, 4)

# Graph Coloring
# Graph coloring assigns colors to vertices such that no two adjacent vertices have the same color.