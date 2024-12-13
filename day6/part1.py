import os 

num_of_cols_to_create = 130
num_of_rows_to_create = 130
guard_x = 0
guard_y = 0
direction = "up"

board = [[" " for _ in range(num_of_cols_to_create)]
            for _ in range(num_of_rows_to_create)]

def update_warehouse_map(board, row, col, symbol):
    """Takes in coordinates of 2DList and adds the passed symbol"""
    if board[row][col] == " ":
        board[row][col] = symbol
    else:
        print("Cell already taken! Choose another.")

with open("day6\\input.txt", 'r', encoding='utf-8') as file:
    for row, line in enumerate(file):
        for column, alpha in enumerate(line.rstrip('\n')):
            update_warehouse_map(board, row, column, alpha)
            if alpha == "^":
                print(f"Guard found at {row} / {column}")
                guard_x = row
                guard_y = column

def move_up():
    global board, guard_x, guard_y, direction

    if guard_x == 0:
        direction = "win"
        board[guard_x][guard_y] = "X"
    elif board[guard_x-1][guard_y]== "#":
        direction = "right"
    else:
        board[guard_x][guard_y] = "X"
        guard_x = guard_x-1

def move_down():
    global board, guard_x, guard_y, direction

    if guard_x == (num_of_cols_to_create-1):
        direction = "win"
        board[guard_x][guard_y] = "X"
    elif board[guard_x+1][guard_y] == "#":
        direction = "left"
    else:
        board[guard_x][guard_y] = "X"
        guard_x = guard_x+1

def move_right():
    global board, guard_x, guard_y, direction

    if guard_y == (num_of_cols_to_create-1):
        direction = "win"
        board[guard_x][guard_y] = "X"
    elif board[guard_x][guard_y+1] == "#":
        direction = "down"
    else:
        board[guard_x][guard_y] = "X"
        guard_y = guard_y+1

def move_left():
    global board, guard_x, guard_y, direction

    if guard_y == 0:
        direction = "win"
        board[guard_x][guard_y] = "X"
    elif board[guard_x][guard_y-1] == "#":
        direction = "up"
    else:
        board[guard_x][guard_y] = "X"
        guard_y = guard_y-1

while direction != "win":
    if direction == "up":
        move_up()
    elif direction == "right":
        move_right()
    elif direction == "down":
        move_down()
    elif direction == "left":
        move_left()

count = 0
for row in board:
    count += row.count("X")

print(count)





