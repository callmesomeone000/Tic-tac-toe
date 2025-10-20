import random

# --- Game Setup ---
board = ['-'] * 9
current_player = 'X'
winner = None
game_running = True

# --- Functions ---
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def player_input(board):
    while True:
        try:
            inp = int(input("Enter a number (1-9): "))
            if inp in range(1, 10) and board[inp - 1] == '-':
                board[inp - 1] = current_player
                break
            else:
                print("❌ Spot taken or invalid. Try again.")
        except ValueError:
            print("⚠️ Please enter a valid number between 1-9.")

def check_horizontal(board):
    global winner
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != '-':
            winner = board[i]
            return True
    return False

def check_vertical(board):
    global winner
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != '-':
            winner = board[i]
            return True
    return False

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True
    return False

def check_win(board):
    if check_horizontal(board) or check_vertical(board) or check_diagonal(board):
        print_board(board)
        print(f"🏆 The winner is {winner}!")
        return True
    return False

def check_tie(board):
    if '-' not in board:
        print_board(board)
        print("🤝 It's a tie!")
        return True
    return False

def switch_player():
    global current_player
    current_player = 'O' if current_player == 'X' else 'X'

def computer_move(board):
    print("💻 Computer's turn...")
    while True:
        pos = random.randint(0, 8)
        if board[pos] == '-':
            board[pos] = 'O'
            break

# --- Game Loop ---
mode = input("Play vs (1) Player or (2) Computer? Enter 1 or 2: ")

while game_running:
    print_board(board)

    if mode == '1' or (mode == '2' and current_player == 'X'):
        player_input(board)
    else:
        computer_move(board)

    if check_win(board) or check_tie(board):
        break

    switch_player()
