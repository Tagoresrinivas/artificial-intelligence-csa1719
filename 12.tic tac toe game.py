def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
   
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board, player):
    
    win_conditions = [
        # Horizontal
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Vertical
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonal
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def check_tie(board):
   
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(player):
    
    while True:
        try:
            row = int(input(f"Player {player}, enter your move row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter your move column (1-3): ")) - 1
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def play_game():
    """Main function to play the game."""
    board = initialize_board()
    current_player = "X"
    
    while True:
        print_board(board)
        row, col = get_player_move(current_player)
        
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("This position is already taken. Please choose another.")
            continue
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
