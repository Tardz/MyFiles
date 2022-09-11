def new_board():
    new_board = []
    return new_board

def find_player(player):
    if player == "player1":
        find_player = "player2" 
    else:
        find_player = "player1"

    return find_player

def get_piece(board, column, row):
    for location in board:
        if (column, row, "player1") == location or (column, row, "player2") == location:
            return str(location[2])

def is_free(board, column, row):
    player = get_piece(board, column, row)

    if (column, row, player) in board:
        return False
    else:
        return True

def place_piece(board, column, row, player):
    other_player = find_player(player)
    location = (column, row, other_player)
    place_location = (column, row, player)

    if location in board:
        return False
    else:
        board.append(place_location)
        return True

def remove_piece(board, column, row):
    player = get_piece(board, column, row)
    
    for location in board:
        if (column, row, player) == location:
            board.remove(location)
            return True
        else:
            return False

def move_piece(board, column, row, new_column, new_row):
    player = get_piece(board, column, row)
    other_player = find_player(player)

    if (column, row, player) in board:
        if (new_column, new_row, player) in board or (new_column, new_row, other_player) in board:
            return False
        else:
            board.remove((column, row, player))
            board.append((new_column, new_row, player))
            return True      
    else:
        return False 

def count(board, row_or_column, number, player):
    result = 0
    if row_or_column == "column":
        for column_item in board:
            if (number, row, player) == column_item:
                result += 1




#def nearest_piece():

board = new_board()
print(place_piece(board, 500, 100, "player2"))
print(place_piece(board, 600, 100, "player1"))
print(board)
print(is_free(board, 500, 100))
print(get_piece(board, 600, 100))
print(board)
print(move_piece(board, 600, 100, 400, 100))
print(board)

