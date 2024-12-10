"""Module testing AoC 2024 day4 part 1"""
import unittest
import os
from day4.day4_pt2_solution import (
    create_empty_board,
    count_word_occurence
)


class TestWordSearch(unittest.TestCase):

    def test_find_MAS_9(self):
        here = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(here, 'test-input.txt')
        words_to_find = ['MAS']
        # Example: Create a 10x10 board
        rows, cols = 10, 10
        game_board = create_empty_board(rows, cols, file_name)
        xmas_count = count_word_occurence(game_board, words_to_find)
        print(f"Count of X-MAS: {xmas_count}")
        self.assertEqual(xmas_count, 9, "these are not equal")

    def test_find_MAS_real(self):
        here = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(here, 'input.txt')
        words_to_find = ['MAS']
        # Example: Create a 140x140 board
        rows, cols = 140, 140
        game_board = create_empty_board(rows, cols, file_name)
        xmas_count = count_word_occurence(game_board, words_to_find)
        print(f"Count of X-MAS: {xmas_count}")
        self.assertEqual(xmas_count, 1998, "these are not equal")

if __name__ == "__main__":
    unittest.main(verbosity=2)
