def is_valid(graph, colors, node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def map_coloring(graph, colors, node, m):
    if node == len(graph):
        return True  # All nodes have been successfully colored
    
    for color in range(1, m + 1):
        if is_valid(graph, colors, node, color):
            colors[node] = color
            if map_coloring(graph, colors, node + 1, m):
                return True
            colors[node] = 0  # Backtrack
    
    return False

def print_solution(colors):
    region_names = ['Region ' + str(i) for i in range(len(colors))]
    for name, color in zip(region_names, colors):
        print(f"{name}: Color {color}")

# Example usage
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
m = 3  # Number of colors
colors = [0] * len(graph)

if map_coloring(graph, colors, 0, m):
    print_solution(colors)
else:
    print("Solution does not exist.")
