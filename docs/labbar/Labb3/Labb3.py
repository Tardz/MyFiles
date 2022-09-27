# -*- coding: utf-8 -*-
### UPPGIFT 3A ###
def new_board():
    new_board = {}
    return new_board

def is_free(board, column, row):
    if (column, row) in board:
        return False
    else:
        return True

def place_piece(board, column, row, player):
    if is_free(board, column, row):
        board[(column, row)] = player
        return True
    else:
        return False
    
def get_piece(board, column, row):
    if is_free(board, column, row):
        return False
    else:
        found = board.get((column, row))
        return found

def remove_piece(board, column, row):
    if is_free(board, column, row):
        return False
    else:
        board.pop((column, row))
        return True

def move_piece(board, column, row, new_column, new_row):
    if is_free(board, column, row):
        return False
    else:
        board[(new_column, new_row)] = board[(column, row)]
        remove_piece(board, column, row)
        return True

def count(board, column_or_row, number, player):
    total_of_players = 0

    if column_or_row == "column":
        for element in board:
            if element[0] == number and get_piece(board, element[0], element[1]) == player:
                total_of_players += 1
    elif column_or_row == "row":
        for element in board:
            if element[1] == number and get_piece(board, element[0], element[1]) == player:
                total_of_players += 1
    else:
        return False
    
    return total_of_players

def nearest_piece(board, column, row):
    if not board:
        return False
    
    current_pythagorean = (column**2 + row**2)**0.5
    shortest_path = -1
    
    for element in board:
        pythagorean = (element[0]**2 + element[1]**2)**0.5
        difference = current_pythagorean - pythagorean
        
        if difference < 0:
            difference = difference*-1

        if shortest_path == -1:
            shortest_path = difference
        elif shortest_path < difference:
            shortest_path = shortest_path
        else:
            shortest_path = difference
    
    for element in board:
        if ((current_pythagorean - ((element[0]**2 + element[1]**2)**0.5))**2)**0.5 == shortest_path:
            return element[0:2]

### UPPGIFT 3B ###
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

def simplify_calculation(n, k): 
    if k < 2:
        return n 
    else:
        k -= 1
        return n*simplify_calculation((n-1), k)

def choose(n, k):
    if (n-k) == 0:
        return 1
    elif k > (n-k):
        return simplify_calculation(n, (n - k))//factorial(n-k)
    else:
        return simplify_calculation(n, k)//factorial(k)