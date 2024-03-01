from collections import deque

def is_valid(state):
    ml, cl, _, mr, cr = state
    # Check if the number of missionaries is 0 or more than cannibals on both sides, or if there are no missionaries
    return (ml == 0 or ml >= cl) and (mr == 0 or mr >= cr)

def get_successors(state):
    successors = []
    ml, cl, boat, mr, cr = state
    # Possible moves: (missionaries, cannibals)
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    for m, c in moves:
        if boat:  # Boat on left side
            new_state = (ml - m, cl - c, not boat, mr + m, cr + c)
        else:  # Boat on right side
            new_state = (ml + m, cl + c, not boat, mr - m, cr - c)
        # Check if new state is valid and append
        if is_valid(new_state):
            successors.append(new_state)
    return successors

def bfs(start, goal):
    queue = deque([start])
    visited = set([start])
    parent_map = {start: None}  # To reconstruct the path
    
    while queue:
        current_state = queue.popleft()
        if current_state == goal:
            return reconstruct_path(parent_map, goal)
        
        for successor in get_successors(current_state):
            if successor not in visited:
                queue.append(successor)
                visited.add(successor)
                parent_map[successor] = current_state
    return None

def reconstruct_path(parent_map, state):
    path = []
    while state:
        path.append(state)
        state = parent_map[state]
    path.reverse()
    return path

if __name__ == "__main__":
    start_state = (3, 3, True, 0, 0)  # (Missionaries left, Cannibals left, Boat, Missionaries right, Cannibals right)
    goal_state = (0, 0, False, 3, 3)
    solution = bfs(start_state, goal_state)
    if solution:
        for step in solution:
            print(step)
    else:
        print("No solution found.")
