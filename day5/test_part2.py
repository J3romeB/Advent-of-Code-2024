"""Testing AoC 2024 day5 part 1"""
import unittest
import os

from day5.solution_part2 import (
    find_middle_value,
    generate_printing_rules_and_instructions,
    get_printing_instructions,
    get_rules,
    validate_instructions
)


class TestPrintingUpdates2(unittest.TestCase):
    """I do the testing of Part 2"""

    @classmethod
    def setUpClass(cls):
        here = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(here, "test-input.txt")
        generate_printing_rules_and_instructions(file_name)

    def test_generate_printing_rules(self):
        """tests that rules and instructions are loading correctly"""
        rules = get_rules()
        rule_key_exists = rules["47|53"]
        self.assertTrue(rule_key_exists, "Key 47|53 Should exist")

        instructions = get_printing_instructions()
        count = len(instructions)
        # Only on dev input
        self.assertEqual(count, 6, "should have 1, if using test input")

    def test_find_middle_value(self):
        """takes a list of integers and returns the middle value"""
        value = [75,47,61,53,29]
        middle_value = find_middle_value(value)
        self.assertEqual(middle_value, 61, "Middle value SHOULD be 61")

    def test_validate_instructions(self):
        """main runner"""
        total = validate_instructions()
        self.assertEqual(total, 123, "how many")


if __name__ == "__main__":
    unittest.main(verbosity=2)
