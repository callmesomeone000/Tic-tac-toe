import random

# --- Game Setup ---
board = ['-'] * 9
current_player = 'X'
winner = None


# --- Functions ---

def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def print_number_board():
    print()
    print(" 1 | 2 | 3")
    print("---|---|---")
    print(" 4 | 5 | 6")
    print("---|---|---")
    print(" 7 | 8 | 9")
    print()


def player_input(board):
    while True:
        try:
            inp = int(input(f"Player {current_player}, choose a position (1-9): "))

            if inp >= 1 and inp <= 9:
                if board[inp - 1] == '-':
                    board[inp - 1] = current_player
                    break
                else:
                    print("❌ That spot is already taken.")
            else:
                print("❌ Enter a number from 1 to 9.")

        except ValueError:
            print("⚠️ Please enter a number.")


def check_horizontal(board):
    global winner

    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != '-':
            winner = board[i]
            return True

    return False


def check_vertical(board):
    global winner

    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != '-':
            winner = board[i]
            return True

    return False


def check_diagonal(board):
    global winner

    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True

    if board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True

    return False


def check_win(board):
    if check_horizontal(board) or check_vertical(board) or check_diagonal(board):
        print_board(board)
        print(f"🏆 Player {winner} wins!")
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

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def computer_move(board):
    print("💻 Computer's turn...")

    while True:
        position = random.randint(0, 8)

        if board[position] == '-':
            board[position] = 'O'
            print(f"💻 Computer chose position {position + 1}")
            break


# --- Choose Game Mode ---

while True:
    mode = input(
        "\nPlay against:\n"
        "1. Another Player\n"
        "2. Computer\n"
        "Enter 1 or 2: "
    )

    if mode == '1' or mode == '2':
        break

    print("❌ Please enter 1 or 2.")


# --- Show Number Guide ---

print("\nHere is the position guide:")
print_number_board()

print("You are X.")
if mode == '2':
    print("The computer is O.")


# --- Game Loop ---

while True:

    print_board(board)

    # Player's turn
    if current_player == 'X':
        player_input(board)

    # Computer's turn
    elif mode == '2' and current_player == 'O':
        computer_move(board)

    # Second human player's turn
    else:
        player_input(board)

    # Check for winner or tie
    if check_win(board):
        break

    if check_tie(board):
        break

    # Change turn
    switch_player()
