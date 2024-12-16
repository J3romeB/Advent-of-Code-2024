import os 
import copy

# num_of_cols_to_create = 10
# num_of_rows_to_create = 10
num_of_cols_to_create = 130
num_of_rows_to_create = 130
guard_x = 0
guard_y = 0
direction = "up"
collision_tracker = [()]
inf_loop_count = 0

board = [[" " for _ in range(num_of_cols_to_create)]
            for _ in range(num_of_rows_to_create)]

def clone_board(board_to_copy):
    return copy.deepcopy(board_to_copy)

def update_warehouse_map(board, row, col, symbol):
    """Takes in coordinates of 2DList and adds the passed symbol"""
    board[row][col] = symbol

with open("day6//input.txt", 'r', encoding='utf-8') as file:
    for row, line in enumerate(file):
        for column, alpha in enumerate(line.rstrip('\n')):
            update_warehouse_map(board, row, column, alpha)
            if alpha == "^":
                print(f"Guard found at {row} / {column}")
                guard_x = row
                guard_y = column

og_x = copy.deepcopy(guard_x)
og_y = copy.deepcopy(guard_y)

def move_up(board):
    global guard_x, guard_y, direction, inf_loop_count

    if guard_x == 0:
        direction = "win"
        board[guard_x][guard_y] = "X"
    elif board[guard_x-1][guard_y]== "#":
        direction = "right"
        collision_data = (guard_x, guard_y, direction)
        if collision_data in collision_tracker:
            direction = 'stuck'
            inf_loop_count += 1
        else:
            collision_tracker.append(collision_data)
        #Have I hit this coordinate from this direction before?
        #If yes, direction to stuck
        #If no, add guard or obstacle coordinate to storage
        
    else:
        board[guard_x][guard_y] = "X"
        guard_x = guard_x-1

def move_down(board):
    global guard_x, guard_y, direction, inf_loop_count

    if guard_x == (num_of_cols_to_create-1):
        direction = "win"
        board[guard_x][guard_y] = "X"
    elif board[guard_x+1][guard_y] == "#":
        direction = "left"
        collision_data = (guard_x, guard_y, direction)
        if collision_data in collision_tracker:
            direction = 'stuck'
            inf_loop_count += 1
        else:
            collision_tracker.append(collision_data)
    else:
        board[guard_x][guard_y] = "X"
        guard_x = guard_x+1

def move_right(board):
    global guard_x, guard_y, direction, inf_loop_count

    if guard_y == (num_of_cols_to_create-1):
        direction = "win"
        board[guard_x][guard_y] = "X"
    elif board[guard_x][guard_y+1] == "#":
        direction = "down"
        collision_data = (guard_x, guard_y, direction)
        if collision_data in collision_tracker:
            direction = 'stuck'
            inf_loop_count += 1
        else:
            collision_tracker.append(collision_data)
    else:
        board[guard_x][guard_y] = "X"
        guard_y = guard_y+1

def move_left(board):
    global guard_x, guard_y, direction, inf_loop_count

    if guard_y == 0:
        direction = "win"
        board[guard_x][guard_y] = "X"
    elif board[guard_x][guard_y-1] == "#":
        direction = "up"
        collision_data = (guard_x, guard_y, direction)
        if collision_data in collision_tracker:
            direction = 'stuck'
            inf_loop_count += 1
        else:
            collision_tracker.append(collision_data)
    else:
        board[guard_x][guard_y] = "X"
        guard_y = guard_y-1

clone = clone_board(board)
for r, row_value in enumerate(board):
    for c, alpha in enumerate(row_value):
        alpha = board[r][c]
        if alpha != "#":
            update_warehouse_map(board, r, c, "#")
        
            while True:
                if direction == "up":
                    move_up(board)
                elif direction == "right":
                    move_right(board)
                elif direction == "down":
                    move_down(board)
                elif direction == "left":
                    move_left(board)
                else:
                    #reset game
                    board = clone_board(clone)
                    direction = 'up'
                    guard_x = og_x
                    guard_y = og_y
                    collision_tracker = [()]
                    break

print(inf_loop_count)

# Loop over every space. Add a #
# Run the game logic.abs
# when you encounter an obstacle. capture it's coordinates and the direction the guard was moving
# If you notice the same obstacle coordinate and same direction you are in a loop.
# or if the guard finished the maze
# Add whatever postion you were at or a counter to the tally.abs
# Reset the game board, and move to the next location to add an obstacle



