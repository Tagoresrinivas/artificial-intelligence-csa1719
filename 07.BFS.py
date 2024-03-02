from collections import deque

def bfs(graph, start):
    visited = set()  # Keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the start node
    visited_order = []  # List to store the order of visited nodes

    while queue:
        vertex = queue.popleft()  # Pop the first vertex in the queue
        if vertex not in visited:
            visited.add(vertex)  # Mark the vertex as visited
            visited_order.append(vertex)  # Add to visited order list
            
            # Add neighbors of the vertex to the queue if not visited
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    
    return visited_order

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform BFS from vertex 'A'
print(bfs(graph, 'A'))
