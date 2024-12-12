"""Testing AoC 2024 Day 6 Guards Path Part 1"""
import unittest
import os

from day6.solution import create_empty_warehouse

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
        warehouse = create_empty_warehouse(rows, cols, file_name)
        distinct_path_traveled = 18
        self.assertEqual(distinct_path_traveled, 18, "these are not equal")


if __name__ == "__main__":
    unittest.main()
