"""Solution to AoC 2024 day4 part 1"""


def build_word_search(file_name, game_board):
    """Takes in a file and created 2DList"""
    with open(file_name, 'r', encoding='utf-8') as file:
        for r, line in enumerate(file):
            for c, alpha in enumerate(line.rstrip('\n')):
                update_board(game_board, r, c, alpha)


def update_board(board, row, col, symbol):
    """Takes in coordinates of 2DList and adds the passed symbol"""
    if board[row][col] == " ":
        board[row][col] = symbol
    else:
        print("Cell already taken! Choose another.")


def create_empty_board(num_of_rows_to_create, num_of_cols_to_create, file_location):
    """Takes in size of 2DList and creates board filled with spaces"""
    # Create a 2D list filled with empty spaces
    board = [[" " for _ in range(num_of_cols_to_create)]
             for _ in range(num_of_rows_to_create)]
    build_word_search(file_location, board)
    return board


def count_word_occurence(board, words_to_find):
    """Takes in 2DList board, and array list of words to find"""
    word_currently_counting = words_to_find[0]
    current_word_count = 0
    letters_checked = 0
    # Can also use the last letter to make searching backwards without needing to loop too much
    letter_that_triggers_search = word_currently_counting[1]
    for r, row in enumerate(board):
        for c, alpha in enumerate(row):
            alpha = board[r][c]
            letters_checked +=1
            if alpha == letter_that_triggers_search:
                # start searching
                if search_diagnol_up_right_and_down_left(word_currently_counting, board, r, c) and search_diagnol_up_left_and_down_right(word_currently_counting, board, r, c):
                    current_word_count +=1

    return current_word_count

def search_diagnol_up_right_and_down_left(word_currently_counting, board, current_row, current_column):
    """Search diagnol up left from passed position"""
    result = False
    #Up Right = -1 Row +1 Column
    row_number_to_check = current_row-1
    column_number_to_check = current_column+1
    if row_number_to_check >= 0 and column_number_to_check < len(board):
        letter_at_coordinate = board[row_number_to_check][column_number_to_check]
        if letter_at_coordinate == "S":
            #Look for an M Down Left = +1 Row -1 Column
            row_number_to_check = current_row+1
            column_number_to_check = current_column-1
            if row_number_to_check < len(board) and column_number_to_check >= 0:
                letter_at_coordinate = board[row_number_to_check][column_number_to_check]
                if letter_at_coordinate == "M":
                    return True
        elif letter_at_coordinate == "M":
            #Look for an S Down Right = +1 Row +1 Column
            row_number_to_check = current_row+1
            column_number_to_check = current_column-1
            if row_number_to_check < len(board) and column_number_to_check >= 0:
                letter_at_coordinate = board[row_number_to_check][column_number_to_check]
                if letter_at_coordinate == "S":
                    return True
    return result

def search_diagnol_up_left_and_down_right(word_currently_counting, board, current_row, current_column):
    """Search diagnol up left from passed position"""
    result = False
    #Up Left = -1 Row -1 Column
    row_number_to_check = current_row-1
    column_number_to_check = current_column-1
    if row_number_to_check >= 0 and column_number_to_check >= 0:
        letter_at_coordinate = board[row_number_to_check][column_number_to_check]
        if letter_at_coordinate == "S":
            #Look for an M Down Right = +1 Row +1 Column
            row_number_to_check = current_row+1
            column_number_to_check = current_column+1
            if row_number_to_check < len(board) and column_number_to_check < len(board):
                letter_at_coordinate = board[row_number_to_check][column_number_to_check]
                if letter_at_coordinate == "M":
                    return True
        elif letter_at_coordinate == "M":
            #Look for an S Down Right = +1 Row +1 Column
            row_number_to_check = current_row+1
            column_number_to_check = current_column+1
            if row_number_to_check < len(board) and column_number_to_check < len(board):
                letter_at_coordinate = board[row_number_to_check][column_number_to_check]
                if letter_at_coordinate == "S":
                    return True
    return result

# Find an A
# look up right for an M or S depending on what you find look for the other letter down search_diagnol_up_left
# if you found both of those, do the same thing but for up left / down right