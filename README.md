# Console-Based Tic-Tac-Toe Game

A simple, interactive two-player Tic-Tac-Toe game implemented in Python. Players take turns marking spaces on a 3x3 grid, aiming to get three of their symbols in a row (horizontally, vertically, or diagonally).

## Features

- Two-player gameplay (X and O)
- Interactive console-based interface
- Input validation and error handling
- Clear visual representation of the game board
- Win and draw detection
- Option to play multiple games
- Simple and intuitive position numbering system

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the `tic_tac_toe.py` file
2. No additional packages are required

## How to Play

1. Run the game:
   ```bash
   python3 tic_tac_toe.py
   ```

2. The game board positions are numbered 1-9 as follows:
   ```
    1 | 2 | 3 
   -----------
    4 | 5 | 6 
   -----------
    7 | 8 | 9 
   ```

3. Players take turns entering a number (1-9) to place their symbol (X or O) in the corresponding position
4. The game continues until one player wins or the game ends in a draw
5. After each game, players can choose to play again

## Game Rules

1. Player 1 uses 'X' and Player 2 uses 'O'
2. Players take turns placing their symbols
3. The first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins
4. If all spaces are filled and no player has won, the game is a draw

## Code Structure

- `print_board(board)`: Displays the current game board
- `check_winner(board)`: Checks if there's a winner
- `is_board_full(board)`: Checks if the board is full (draw condition)
- `get_player_move(player, board)`: Gets and validates player moves
- `main()`: Controls the main game loop

## Error Handling

The game includes error handling for:
- Invalid input (non-numeric values)
- Out-of-range moves (numbers less than 1 or greater than 9)
- Attempting to place a symbol in an occupied position

## Author

[Abdur Rahman]
