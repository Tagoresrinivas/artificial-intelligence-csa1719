def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col, n):
    # Base case: If all queens are placed
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_nq_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0  # Backtrack

    # If the queen cannot be placed in any row in this column col, return False
    return False

def solve_nq(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_nq_util(board, 0, n):
        print("Solution does not exist")
        return False

    # A solution exists
    print_solution(board)
    return True

def print_solution(board):
    for row in board:
        print(" ".join(["Q" if col == 1 else "." for col in row]))

if __name__ == "__main__":
    # Number of Queens
    n = 8
    solve_nq(n)
