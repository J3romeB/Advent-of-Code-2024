"""Module testing AoC 2024 day4 part 1"""
import unittest
import os
from day4.day4_solution import (
    search_right,
    search_left,
    search_down,
    search_up,
    search_diagnol_up_left,
    search_diagnol_down_left,
    search_diagnol_down_right,
    search_diagnol_up_right,
    count_word_occurence,
    create_empty_board
)


class TestWordSearch(unittest.TestCase):
    def test_search_right_when_no_match(self):
        word_currently_counting = "XMAS"
        row = ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M']
        c = 4
        result = search_right(word_currently_counting, row, c)
        self.assertFalse(result, "Should NOT have found a MATCH")

    def test_search_right_when_match(self):
        word_currently_counting = "XMAS"
        row = ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M']
        c = 5
        result = search_right(word_currently_counting, row, c)
        self.assertTrue(result, "Should HAVE found a MATCH")

    def test_search_left_when_match(self):
        word_currently_counting = "XMAS"
        row = ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A']
        c = 4
        result = search_left(word_currently_counting, row, c)
        self.assertTrue(result, "Should HAVE found a MATCH")

    def test_search_left_and_right_sharing_same_S(self):
        word_currently_counting = "XMAS"
        row = ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'M', 'S', 'A'] #xmasamx
        c_right = 0
        c_left = 6
        result = search_left(word_currently_counting, row, c_left)
        self.assertTrue(result, "Should HAVE found a MATCH")
        self.assertTrue(search_right(word_currently_counting, row, c_right))

    def test_search_down_when_match(self):
        board = [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'], ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'], ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'], ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'], ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'], [
            'X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'], ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'], ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'], ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'], ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']]
        word_currently_counting = "XMAS"
        c = 9
        r = 3
        result = search_down(word_currently_counting, board, r, c)
        self.assertTrue(result, "Should HAVE found a MATCH")

    def test_search_up_when_match(self):
        board = [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'], ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'], ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'], ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'], ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'], [
            'X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'], ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'], ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'], ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'], ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']]
        word_currently_counting = "XMAS"
        c = 6
        r = 4
        result = search_up(word_currently_counting, board, r, c)
        self.assertTrue(result, "Should HAVE found a MATCH")

    def test_search_diagnoal_up_right_when_match(self):
        board = [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'], ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'], ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'], ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'], ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'], [
            'X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'], ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'], ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'], ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'], ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']]
        word_currently_counting = "XMAS"
        c = 0
        r = 5
        result = search_diagnol_up_right(word_currently_counting, board, r, c)
        self.assertTrue(result, "Should HAVE found a MATCH")

    def test_search_diagnoal_down_right_when_match(self):
        board = [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'], ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'], ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'], ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'], ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'], [
            'X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'], ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'], ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'], ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'], ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']]
        word_currently_counting = "XMAS"
        c = 4
        r = 0
        result = search_diagnol_down_right(
            word_currently_counting, board, r, c)
        self.assertTrue(result, "Should HAVE found a MATCH")

    def test_search_diagnoal_down_left_when_match(self):
        board = [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'], ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'], ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'], ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'], ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'], [
            'X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'], ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'], ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'], ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'], ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']]
        word_currently_counting = "XMAS"
        c = 9
        r = 3
        result = search_diagnol_down_left(word_currently_counting, board, r, c)
        self.assertTrue(result, "Should HAVE found a MATCH")
        c = 4
        r = 0
        result = search_diagnol_down_left(word_currently_counting, board, r, c)
        self.assertFalse(result, "Should NOT found a MATCH")

    def test_search_diagnoal_up_left_when_match(self):
        board = [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'], ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'], ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'], ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'], ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'], [
            'X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'], ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'], ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'], ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'], ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']]
        word_currently_counting = "XMAS"
        c = 6
        r = 5
        result = search_diagnol_up_left(word_currently_counting, board, r, c)
        self.assertTrue(result, "Should HAVE found a MATCH")
    
    def test_find_XMAS_18(self):
        here = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(here, 'test-input.txt')
        words_to_find = ['XMAS']
        # Example: Create a 10x10 board
        rows, cols = 10, 10
        game_board = create_empty_board(rows, cols, file_name)
        xmas_count = count_word_occurence(game_board, words_to_find)
        print(f"Count of XMAS: {xmas_count}")
        self.assertEqual(xmas_count, 18, "these are not equal")

    def test_find_XMAS_8_from_same_X(self):
        here = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(here, 'test_input_8_from_same_X.txt')
        words_to_find = ['XMAS']
        # Example: Create a 10x10 board
        rows, cols = 10, 10
        game_board = create_empty_board(rows, cols, file_name)
        xmas_count = count_word_occurence(game_board, words_to_find)
        print(f"Count of XMAS: {xmas_count}")
        self.assertEqual(xmas_count, 8, "these are not equal")

    def test_find_XMAS_2569_real(self):
        here = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(here, 'input.txt')
        words_to_find = ['XMAS']
        # Example: Create a 140x140 board
        rows, cols = 140, 140
        game_board = create_empty_board(rows, cols, file_name)
        xmas_count = count_word_occurence(game_board, words_to_find)
        print(f"Count of XMAS: {xmas_count}")
        self.assertEqual(xmas_count, 2569, "these are not equal")

if __name__ == "__main__":
    unittest.main(verbosity=2)
