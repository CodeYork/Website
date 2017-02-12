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
    for i in range(0, 2):
        # check row i
        if board[i][0] == board[i][1] == board[i][2] == player_char:
            return True
        # check col i
        if board[0][i] == board[1][i] == board[2][i] == player_char:
            return True
    # check \
    if board[0][0] == board[1][1] == board[2][2] == player_char:
        return True
    # check /
    if board[2][0] == board[1][1] == board[0][2] == player_char:
        return True
        
    return False

def is_draw(board):
    """
    Return True if neither player
    has won and the board is full.
    """
    if has_won(board, 'X') or has_won(board, 'O'):
        return False
    else:
        return is_full(board)

def is_full(board):
    """
    Return True if game board is full.
    """
    for row in board:
        for el in row:
            if el == None:
                return False
    return True

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
