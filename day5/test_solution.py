"""Testing AoC 2024 day5 part 1"""
import unittest
import os

from solution import find_middle_value, generate_printing_rules_and_instructions, get_printing_instructions, get_rules, validate_instructions


class TestPrintingUpdates(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        here = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(here, "test-input.txt")
        generate_printing_rules_and_instructions(file_name)

    def test_generate_printing_rules(self):
        rules = get_rules()
        rule_key_exists = rules["47|53"]
        self.assertTrue(rule_key_exists, "Key 47|53 Should exist")

        instructions = get_printing_instructions()
        count = len(instructions)
        self.assertEqual(count, 1, "should have 1, if using dev input") # Only on dev input

    def test_find_middle_value(self):
        value = "75,47,61,53,29"
        middle_value = find_middle_value(value)
        self.assertEqual(middle_value, 61, "Middle value SHOULD be 61")

    def test_validate_instructions(self):
        total = validate_instructions()
        self.assertEqual(total, 143, "how many")

if __name__ == "__main__":
    unittest.main(verbosity=2)
