"""AoC 2024 Day 6 Guards Path Part 1 Solution"""
class Guard(object):
    def __init__(self, mylist=[]):
        self.mylist = mylist

def build_warehouse_map(file_name, warehouse_map):
    """Takes in a file and created 2DList"""
    with open(file_name, 'r', encoding='utf-8') as file:
        for row, line in enumerate(file):
            for column, alpha in enumerate(line.rstrip('\n')):
                update_warehouse_map(warehouse_map, row, column, alpha)
                if alpha == "^":
                    print(f"Guard found at {row} / {column}")
                    guard_x = r
                    guard_y = c


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
    return board

class TestGuardPathSolution(unittest.TestCase):
    """Main Testing Class"""

    def test_builing_the_map(self):
        """build the map"""
        None

    def test_count_guards_path_for_test_input(self):
        here = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(here, 'test_input.txt')
        # Example: Create a 10x10 board
        rows, cols = 10, 10
        empty_warehouse = create_empty_warehouse(rows, cols, file_name)
        filled_warehouse = build_warehouse_map(file_location, empty_warehouse)
        distinct_path_traveled = simulate_guards_path(warehouse)
        self.assertEqual(distinct_path_traveled, 18, "these are not equal")


if __name__ == "__main__":
    unittest.main()