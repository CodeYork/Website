"""
Tic tac toe game, for Python.
"""

def play_game():
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    player_char = 'X'
    while not is_game_finished(board):
        print_board(board)
        board = make_move(board, player_char)
        player_char = 'X' if player_char == 'O' else 'O'
    print_winner(board)

def is_game_finished(board):
    """
    Return whether a game is finished or not.
    """
    return has_won(board, 'X') or has_won(board, 'O') or is_draw(board)

def has_won(board, player_char):
    """
    Return whether a player has won or not.
    """
    # TODO: actually check if the given player has won or not
    return False

def is_draw(board):
    """
    Return True if neither player
    has won and all board positions
    are 'None'.
    """
    if not (has_won(board, 'X') or has_won(board, 'O')):
        # TODO: Check if the board is full
        # and return appropriately
        pass
    else:
        return False

def print_board(board):
    # TODO: make this printing prettier
    for row in board:
        print(row)

def make_move(board, player_char):
    """
    Ask for move from player and place
    token there. If move is invalid,
    ask again.
    """
    while True:
        row = int(input("Please choose a row: "))
        col = int(input("Please choose a column: "))
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Remember that 0 <= row, column < 3.")
        elif board[row][col] is None:
            board[row][col] = player_char
            return board
        else:
            print("Please enter an unused position.")

def print_winner(board):
    """
    Print the winner of the game.
    """
    if is_draw(board):
        print("No winner.")
    elif has_won(board, 'X'):
        print("X won!")
    else:
        print("O won!")

play_game()
