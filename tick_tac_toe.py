def print_board(board):
    """Print the current state of the board"""
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3 + 1]} | {board[i*3 + 2]} ")
        if i < 2:
            print("-----------")

def check_winner(board):
    """Check if there's a winner"""
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    
    return None

def is_board_full(board):
    """Check if the board is full"""
    return ' ' not in board

def get_player_move(player, board):
    """Get a valid move from the player"""
    while True:
        try:
            move = int(input(f'Player {player}, enter your move (1-9): ')) - 1
            if 0 <= move < 9 and board[move] == ' ':
                return move
            else:
                print("Invalid move. The position is either occupied or out of range.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def main():
    # Initialize the board
    board = [' '] * 9
    current_player = 'X'
    
    # Print initial game instructions
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is X and Player 2 is O")
    print("Positions are numbered from 1-9 starting from top-left:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("\nLet's begin!\n")

    while True:
        # Print current board state
        print_board(board)
        
        # Get player's move
        move = get_player_move(current_player, board)
        board[move] = current_player
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"\nPlayer {winner} wins!")
            break
        
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("\nIt's a draw!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    while True:
        main()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break