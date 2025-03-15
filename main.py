import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    while True:
        print_board(board)
        player = players[turn % 2]
        
        if player == "X":
            row, col = map(int, input("Enter row and column (0-2): ").split())
        else:
            row, col = random.choice(get_available_moves(board))
            print(f"Computer chose: {row} {col}")
        
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"{player} wins!")
                break
            elif not get_available_moves(board):
                print_board(board)
                print("It's a draw!")
                break
            turn += 1
        else:
            print("Invalid move, try again.")

if __name__ == "__main__":
    tic_tac_toe()
