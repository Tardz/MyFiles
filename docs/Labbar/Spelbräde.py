def new_board():
    new_board = []
    return new_board

def is_free(board, column, row):
    location = (column, row)
    if location in board:
        return False
    else:
        return True

def place_piece(board, column, row, player):
    if player == "player1":
        find_player = "player2" 
    else:
        find_player = "player1"
    
    location = (column, row, find_player)
    place_location = (column, row, player)

    if location in board:
        return False
    else:
        board.append(place_location)
        return True

#def get_piece(current_board, column, row):

#def remove_piece():

#def move_piece():

#def count():

#def nearest_piece():

board = new_board()
print(place_piece(board, 500, 100, "player2"))
print(place_piece(board, 500, 100, "player1"))
print(is_free(board, 500, 100))
