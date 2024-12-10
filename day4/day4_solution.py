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
    letter_that_triggers_search = word_currently_counting[0]
    for r, row in enumerate(board):
        for c, alpha in enumerate(row):
            alpha = board[r][c]
            letters_checked +=1
            if alpha == letter_that_triggers_search:
                # start searching
                if search_right(word_currently_counting, row, c):
                    current_word_count += 1
                    print(f'searching right {r} col {c}')
                if search_left(word_currently_counting, row, c):
                    current_word_count += 1
                    print(f'searching left {r} col {c}')
                if search_down(word_currently_counting, board, r, c):
                    current_word_count += 1
                    print(f'searching down {r} col {c}')
                if search_up(word_currently_counting, board, r, c):
                    current_word_count += 1
                    print(f'searching up {r} col {c}')
                if search_diagnol_up_right(word_currently_counting, board, r, c):
                    current_word_count += 1
                    print(f'searching d u right {r} col {c}')
                if search_diagnol_down_right(word_currently_counting, board, r, c):
                    current_word_count += 1
                    print(f'searching d d right {r} col {c}')
                if search_diagnol_down_left(word_currently_counting, board, r, c):
                    current_word_count += 1
                    print(f'searching d d left {r} col {c}')
                if search_diagnol_up_left(word_currently_counting, board, r, c):
                    current_word_count += 1
                    print(f'searching d u left {r} col {c}')
    print(f'checked {letters_checked} letters')
    return current_word_count


def search_right(word_currently_counting, row, current_index):
    """Search right from passed position"""
    result = False
    current_word_lengh = len(word_currently_counting)
    last_letter_of_current_word = word_currently_counting[-1]
    coordinate_to_check = current_index+current_word_lengh-1
    right_boundry = len(row)
    if coordinate_to_check < right_boundry:
        letter_at_coordinate = row[coordinate_to_check]
        if letter_at_coordinate == last_letter_of_current_word:
            counter = 1
            # just need to check middle letters, already know we are at First postion, and confirmed last position is accurate
            for middle_letters in word_currently_counting[1:-1]:
                next_letter_in_row = row[current_index+counter]
                if next_letter_in_row != middle_letters:
                    return False
                counter += 1
            result = True
    return result


def search_left(word_currently_counting, row, current_index):
    """Search left from passed position"""
    # just invert the word and use the search_rightlogic after seeing if last letter is correct
    result = False
    current_word_lengh = len(word_currently_counting)
    last_letter_of_current_word = word_currently_counting[-1]
    coordinate_to_check = current_index-current_word_lengh+1
    if coordinate_to_check >= 0:
        letter_at_coordinate = row[coordinate_to_check]
        if letter_at_coordinate == last_letter_of_current_word:
            # flip the word and use search right
            reversed_string = word_currently_counting[::-1]
            result = search_right(reversed_string, row, coordinate_to_check)
    return result


def search_down(word_currently_counting, board, current_row, current_column):
    """Search down from passed position"""
    result = False
    current_word_lengh = len(word_currently_counting)
    last_letter_of_current_word = word_currently_counting[-1]
    row_number_to_check = current_row+current_word_lengh - \
        1  # same column but some rows down
    lower_boundry = len(board)-1
    if row_number_to_check <= lower_boundry:  # not more than total rows
        letter_at_coordinate = board[row_number_to_check][current_column]
        if letter_at_coordinate == last_letter_of_current_word:
            counter = 1
            # just need to check middle letters, already know we are at First postion, and confirmed last position is accurate
            for middle_letters in word_currently_counting[1:-1]:
                # row[current_index+counter]
                next_letter_in_row = board[current_row+counter][current_column]
                if next_letter_in_row != middle_letters:
                    return False
                counter += 1
            result = True
    return result


def search_up(word_currently_counting, board, current_row, current_column):
    """Search up from passed position"""
    # just invert the word and use the search_down logic after seeing if last letter is correct
    result = False
    current_word_lengh = len(word_currently_counting)
    last_letter_of_current_word = word_currently_counting[-1]
    row_number_to_check = current_row-current_word_lengh + \
        1  # same column but some rows up
    if row_number_to_check >= 0:
        letter_at_coordinate = board[row_number_to_check][current_column]
        if letter_at_coordinate == last_letter_of_current_word:
            # flip the word and use search right
            reversed_string = word_currently_counting[::-1]
            result = search_down(reversed_string, board,
                                 row_number_to_check, current_column)
    return result


def search_diagnol_up_right(word_currently_counting, board, current_row, current_column):
    """Search diagnol up right from passed position"""
    result = False
    current_word_lengh = len(word_currently_counting)
    last_letter_of_current_word = word_currently_counting[-1]
    row_number_to_check = current_row-current_word_lengh+1  # 2
    column_number_to_check = current_column+current_word_lengh-1  # 3
    if row_number_to_check >= 0 and column_number_to_check < len(board[0]):
        letter_at_coordinate = board[row_number_to_check][column_number_to_check]
        if letter_at_coordinate == last_letter_of_current_word:
            counter = 1
            # just need to check middle letters, already know we are at First postion, and confirmed last position is accurate
            for middle_letters in word_currently_counting[1:-1]:
                next_letter_up_right = board[current_row -
                                             counter][current_column+counter]
                if next_letter_up_right != middle_letters:
                    return False
                counter += 1
            result = True
    return result


def search_diagnol_down_right(word_currently_counting, board, current_row, current_column):
    """Search diagnol down right from passed position"""
    result = False
    current_word_lengh = len(word_currently_counting)
    last_letter_of_current_word = word_currently_counting[-1]
    row_number_to_check = current_row+current_word_lengh-1  # 3
    column_number_to_check = current_column+current_word_lengh-1  # 7
    lower_boundry = len(board)-1
    if row_number_to_check <= lower_boundry and column_number_to_check < len(board[0]):
        letter_at_coordinate = board[row_number_to_check][column_number_to_check]
        if letter_at_coordinate == last_letter_of_current_word:
            counter = 1
            # just need to check middle letters, already know we are at First postion, and confirmed last position is accurate
            for middle_letters in word_currently_counting[1:-1]:
                next_letter_down_right = board[current_row +
                                               counter][current_column+counter]
                if next_letter_down_right != middle_letters:
                    return False
                counter += 1
            result = True
    return result


def search_diagnol_down_left(word_currently_counting, board, current_row, current_column):
    """Search diagnol down left from passed position"""
    result = False
    current_word_lengh = len(word_currently_counting)
    last_letter_of_current_word = word_currently_counting[-1]
    row_number_to_check = current_row+current_word_lengh-1
    column_number_to_check = current_column-current_word_lengh+1
    lower_boundry = len(board)-1
    if row_number_to_check <= lower_boundry and column_number_to_check >= 0:
        letter_at_coordinate = board[row_number_to_check][column_number_to_check]
        if letter_at_coordinate == last_letter_of_current_word:
            counter = 1
            # just need to check middle letters, already know we are at First postion, and confirmed last position is accurate
            for middle_letters in word_currently_counting[1:-1]:
                next_letter_down_left = board[current_row +
                                              counter][current_column-counter]
                if next_letter_down_left != middle_letters:
                    return False
                counter += 1
            result = True
    return result


def search_diagnol_up_left(word_currently_counting, board, current_row, current_column):
    """Search diagnol up left from passed position"""
    result = False
    current_word_lengh = len(word_currently_counting)
    last_letter_of_current_word = word_currently_counting[-1]
    row_number_to_check = current_row-current_word_lengh+1
    column_number_to_check = current_column-current_word_lengh+1
    if row_number_to_check >= 0 and column_number_to_check >= 0:
        letter_at_coordinate = board[row_number_to_check][column_number_to_check]
        if letter_at_coordinate == last_letter_of_current_word:
            counter = 1
            # just need to check middle letters, already know we are at First postion, and confirmed last position is accurate
            for middle_letters in word_currently_counting[1:-1]:
                next_letter_up_left = board[current_row -
                                            counter][current_column-counter]
                if next_letter_up_left != middle_letters:
                    return False
                counter += 1
            result = True
    return result

# Read in file
# Build the coordinates array
# Example           M       M           M       S       X           XMASM
# First Character (0,0 = M)(0,1 = M)(0,2 = M)(0,3 = S)(0,4 = X)(0,5 = X)
# Array of Arrays
# Ray for Line #0     Array for Position in that Array [0] [1]
# Board / Column / Row
