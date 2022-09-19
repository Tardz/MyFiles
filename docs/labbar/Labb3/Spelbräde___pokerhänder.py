### UPPGIFT 3A ###
def new_board():
    new_board = []
    return new_board

def find_player(player):
    if player == "spelare1":
        find_player = "spelare2" 
    else:
        find_player = "spelare1"

    return find_player

def get_piece(board, column, row):
    for location in board:
        if (column, row, "spelare1") == location or (column, row, "spelare2") == location:
            return str(location[2])

    return False

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
    column = 0
    row = 0

    if row_or_column == "row":
        row = number
        slot = 1
    elif row_or_column == "column":
        column = number
        slot = 0
    else:
        return "Wrong input, variable 2"
    
    location = (column, row, player)
    number_of_places = 0

    for tuple in board:
        if location[slot] == tuple[slot] and location[2] == tuple[2]:
            number_of_places += 1
        
    return number_of_places

def nearest_piece(board, column, row):
    if board == []:
        return False
        
    current_pythagorean = (column**2 + row**2)**0.5
    shortest_path = -1

    for tuple in board:
        pythagorean_first = (tuple[0]**2 + tuple[1]**2)**0.5
        difference_first = current_pythagorean - pythagorean_first
        
        if difference_first < 0:
            difference_first = difference_first * -1

        if shortest_path == -1:
            shortest_path = difference_first
        elif shortest_path < difference_first:
            shortest_path = shortest_path
        else:
            shortest_path = difference_first
    
    for tuple in board:
        if ((current_pythagorean - ((tuple[0]**2 + tuple[1]**2)**0.5))**2)**0.5 == shortest_path:
            return tuple[0:2]

### UPPGIFT 3B ###
def factorial(n):
    if n == 1 or 0:
        return 1

    length = 2
    result = n * (n-1)

    for number in range(n-2):
            result = result * (n - length)
            length += 1

    return result

def choose(n, k):
    if k == 0:
        return 1
    elif n == k:
        return 1
    elif n > k:
        return (factorial(n)/(factorial(k)*factorial(n-k)))
    else:
        return False

print(choose(10, 0))