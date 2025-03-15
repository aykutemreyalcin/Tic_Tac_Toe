# Tic-Tac-Toe in Python

## Overview
This Python program implements a simple **Tic-Tac-Toe game**, where a human player competes against a basic AI (random move selection).

## How It Works
1. The game board is displayed.
2. The human player (`X`) enters their move by specifying row and column indices.
3. The AI (`O`) randomly selects an available move.
4. The game continues until:
   - A player wins.
   - The board is full (resulting in a draw).
5. The program announces the result and displays the final board state.

## Installation & Usage

### Requirements
- Python 3.x

### Running the Game
```sh
python tic_tac_toe.py
```

### Expected Output
```
  |   |  
---------
  |   |  
---------
  |   |  
Enter row and column (0-2): 1 1
  |   |  
---------
  | X |  
---------
  |   |  
Computer chose: 0 2
```