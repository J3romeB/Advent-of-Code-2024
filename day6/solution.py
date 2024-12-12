"""AoC 2024 Day 6 Guards Path Part 1 Solution"""
position = [][]

def build_warehouse_map(file_name, warehouse_map):
    """Takes in a file and created 2DList"""
    with open(file_name, 'r', encoding='utf-8') as file:
        for r, line in enumerate(file):
            for c, alpha in enumerate(line.rstrip('\n')):
                update_warehouse_map(warehouse_map, r, c, alpha)
                if alpha == "^":
                    position = [r][c]


def update_warehouse_map(board, row, col, symbol):
    """Takes in coordinates of 2DList and adds the passed symbol"""
    if board[row][col] == " ":
        board[row][col] = symbol
    else:
        print("Cell already taken! Choose another.")


def create_empty_warehouse(num_of_rows_to_create, num_of_cols_to_create, file_location):
    """Takes in size of 2DList and creates board filled with spaces"""
    # Create a 2D list filled with empty spaces
    board = [[" " for _ in range(num_of_cols_to_create)]
             for _ in range(num_of_rows_to_create)]
    build_warehouse_map(file_location, board)
    return board