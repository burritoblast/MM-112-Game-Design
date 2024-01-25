import random

board = [['-' for _ in range(4)] for _ in range(4)]

def is_valid(row, col, unplayable_square):
    row -= 1
    col -= 1
    return 0 <= row < 4 and 0 <= col < 4 and board[row][col] == '-' and (row, col) != unplayable_square

def print_board(unplayable_square):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if (i + 1, j + 1) == unplayable_square:
                print('@', end=' ')
            else:
                print(cell, end=' ')
        print()

def has_won(symbol):
    for row in range(4):
        if any(all(board[row][col] == symbol for col in range(c, c + 3)) for c in range(2)):
            return True

    for col in range(4):
        if any(all(board[row][col] == symbol for row in range(r, r + 3)) for r in range(2)):
            return True

    if any(all(board[i][i] == symbol for i in range(d, d + 3)) for d in range(2)):
        return True
    if any(all(board[i][3 - i] == symbol for i in range(d, d + 3)) for d in range(2)):
        return True

    return False


def make_move(row, col, symbol):
    row -= 1
    col -= 1
    board[row][col] = symbol

def get_move(unplayable_square):
    while True:
        row = int(input("Enter row (Vertical) (1-4): "))
        col = int(input("Enter column (Horizontal) (1-4): "))
        
        if row < 1 or row > 4 or col < 1 or col > 4:
            print("Row and column must be between 1-4!")
            continue
        
        if is_valid(row, col, unplayable_square):
            return (row, col)
            
        print("Invalid move!")

def play_again():
    play_again_input = input("Do you want to play again? (yes/no): ")
    return play_again_input.lower() == 'yes'

def play_game():
    global board
    current_player = 'X'
    unplayable_square = (random.randint(1, 4), random.randint(1, 4))

    while True:
        print("Unplayable square:", unplayable_square)
        print_board(unplayable_square)

        move = get_move(unplayable_square)
        make_move(move[0], move[1], current_player)

        if has_won(current_player):
            print(current_player, "wins!")
            if not play_again():
                return
            else:
                board = [['-' for _ in range(4)] for _ in range(4)]
                unplayable_square = (random.randint(1, 4), random.randint(1, 4))

        if all(cell != '-' for row in board for cell in row):
            print("It's a tie!")
            if not play_again():
                return
            else:
                board = [['-' for _ in range(4)] for _ in range(4)]
                unplayable_square = (random.randint(1, 4), random.randint(1, 4))

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

play_game()
