import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Check ro0ws
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def player_move(board):
    while True:
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = "X"
            break
        else:
            print("That cell is already taken. Try again.")

def computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if board[row][col] == " ":
            board[row][col] = "O"
            break

def main():
    board = [[" "]*3 for _ in range(3)]

    while True:
        print_board(board)
        player_move(board)

        if check_winner(board):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        print("Computer's Turn:")
        computer_move(board)

        if check_winner(board):
            print_board(board)
            print("Sorry, the computer wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
