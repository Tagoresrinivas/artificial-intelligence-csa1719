from itertools import permutations

def calculate_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route)):
        total_distance += distance_matrix[route[i-1]][route[i]]
    return total_distance

def tsp_brute_force(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    min_route = None
    min_distance = float('inf')
    
    for route in permutations(cities):
        current_distance = calculate_distance(route, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            min_route = route
            
    return min_distance, min_route

# Example usage
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_distance, min_route = tsp_brute_force(distance_matrix)
print(f"Minimum distance: {min_distance}")
print(f"Route: {min_route}")
