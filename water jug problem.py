from collections import deque

def get_all_states(state):
    """
    Return a list of all possible states from the current state.
    Args:
    - state: A tuple (jug1, jug2) representing the current state
    
    Returns:
    - A list of tuples representing all possible next states
    """
    x, y = state
    # Maximum capacities of the two jugs
    max_x, max_y, target = capacity_x, capacity_y, target_amount
    # Generate all possible next states
    return [
        (max_x, y) if x < max_x else (x, y),  # Fill Jug1
        (x, max_y) if y < max_y else (x, y),  # Fill Jug2
        (0, y) if x > 0 else (x, y),  # Empty Jug1
        (x, 0) if y > 0 else (x, y),  # Empty Jug2
        (x - min(x, max_y - y), y + min(x, max_y - y)) if x > 0 else (x, y),  # Pour Jug1 to Jug2
        (x + min(y, max_x - x), y - min(y, max_x - x)) if y > 0 else (x, y),  # Pour Jug2 to Jug1
    ]

def water_jug_solver(capacity_x, capacity_y, target_amount):
    """
    Solve the water jug problem.
    
    Args:
    - capacity_x: Capacity of Jug1
    - capacity_y: Capacity of Jug2
    - target_amount: Target amount of water to achieve in either jug
    
    Returns:
    - A list of actions to achieve the target amount, or None if no solution.
    """
    visited = set()
    queue = deque([(0, 0)])  # Initial state: both jugs are empty

    while queue:
        current_state = queue.popleft()
        if current_state in visited:
            continue
        visited.add(current_state)
        # Check if the current state solves the problem
        if target_amount in current_state:
            return True
        # Add all possible next states to the queue
        for next_state in get_all_states(current_state):
            if next_state not in visited:
                queue.append(next_state)
    return False

if __name__ == "__main__":
    capacity_x, capacity_y, target_amount = 4, 3, 2  # Example capacities and target
    if water_jug_solver(capacity_x, capacity_y, target_amount):
        print("Solution exists")
    else:
        print("No solution")
