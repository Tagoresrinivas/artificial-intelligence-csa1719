import math

def evaluate(board):
    # Check rows, columns, and diagonals for a win or loss
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '-':
            return 10 if board[row][0] == 'X' else -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '-':
            return 10 if board[0][col] == 'X' else -10
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return 10 if board[0][0] == 'X' else -10
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return 10 if board[0][2] == 'X' else -10
    return 0  # No winner

def minimax(board, depth, is_maximizer):
    score = evaluate(board)

    # If the game is over, return the score
    if score == 10 or score == -10:
        return score

    # If there are no moves left, it's a draw
    if not any('-' in row for row in board):
        return 0

    if is_maximizer:
        best = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == '-':
                    board[row][col] = 'X'
                    best = max(best, minimax(board, depth+1, not is_maximizer))
                    board[row][col] = '-'
        return best
    else:
        best = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == '-':
                    board[row][col] = 'O'
                    best = min(best, minimax(board, depth+1, not is_maximizer))
                    board[row][col] = '-'
        return best

def find_best_move(board):
    best_move = (-1, -1)
    best_val = -math.inf
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                board[row][col] = 'X'
                move_val = minimax(board, 0, False)
                board[row][col] = '-'
                if move_val > best_val:
                    best_move = (row, col)
                    best_val = move_val
    return best_move

def print_board(board):
    for row in board:
        print(' '.join(row))

if __name__ == "__main__":
    # Example usage:
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    
    # Play until game over
    while True:
        print("Current board:")
        print_board(board)

        # Player's move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        board[row][col] = 'O'

        # Check if player wins
        if evaluate(board) == -10:
            print("You win!")
            break

        # AI's move
        print("AI's move:")
        row, col = find_best_move(board)
        board[row][col] = 'X'

        # Check if AI wins
        if evaluate(board) == 10:
            print("AI wins!")
            break

        # Check for draw
        if not any('-' in row for row in board):
            print("It's a draw!")
            break
