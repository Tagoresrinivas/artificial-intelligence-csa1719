import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def calculate_heuristic(self):
        # Manhattan distance heuristic
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        heuristic = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_i, goal_j = divmod(self.state[i][j] - 1, 3)
                    heuristic += abs(i - goal_i) + abs(j - goal_j)
        return heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(node):
    i, j = get_blank_position(node.state)
    neighbors = []

    if i > 0:
        neighbors.append(('UP', (i - 1, j)))
    if i < 2:
        neighbors.append(('DOWN', (i + 1, j)))
    if j > 0:
        neighbors.append(('LEFT', (i, j - 1)))
    if j < 2:
        neighbors.append(('RIGHT', (i, j + 1)))

    return neighbors

def apply_action(state, action):
    i, j = get_blank_position(state)
    new_state = [row.copy() for row in state]
    new_i, new_j = action[1]
    new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
    return new_state

def solve_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state)
    frontier = [initial_node]
    explored = set()

    while frontier:
        current_node = heapq.heappop(frontier)

        if current_node.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return get_solution_path(current_node)

        explored.add(tuple(map(tuple, current_node.state)))

        for action, neighbor_pos in get_neighbors(current_node):
            neighbor_state = apply_action(current_node.state, (action, neighbor_pos))

            if tuple(map(tuple, neighbor_state)) not in explored:
                neighbor_node = PuzzleNode(neighbor_state, current_node, action, current_node.cost + 1)
                heapq.heappush(frontier, neighbor_node)

    return None  # No solution found

def get_solution_path(goal_node):
    path = []
    while goal_node.parent is not None:
        path.insert(0, (goal_node.action, goal_node.state))
        goal_node = goal_node.parent
    return path

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 5, 6],
        [0, 7, 8]
    ]

    solution = solve_puzzle(initial_state)

    if solution:
        print("Solution Found:")
        for step, state in solution:
            print(f"Action: {step}, State:")
            for row in state:
                print(row)
            print("----")
    else:
        print("No solution found.")
