"""Testing AoC 2024 day5 part 1"""
import unittest
import os
from day5.solution  import (
    generate_printing_rules_and_instructions,
    find_middle_value,
    get_rules,
    get_printing_instructions,
    validate_instructions
)


class TestPrintingUpdates(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        here = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(here, "test-input.txt")
        generate_printing_rules_and_instructions(file_name)

    def test_correct_order_example(self):
        # 75,47,61,53,29
        # 97,61,53,29,13
        # 75,29,13
        # 47|53 75|47 75|61 75|53 75|29 47|61 47|53 47|29
        None

    def test_incorrect_order_example(self):
        # 75,97,47,61,53
        # 61,13,29
        # 97,13,75,29,47
        None

    def test_generate_printing_rules(self):
        # "47|53"
        rules = get_rules()
        rule_count = len(rules)
        rule_key_exists = rules["47|53"]
        print(f'What is rule_key_exists, {rule_key_exists}')
        self.assertEqual(rule_count, 1, "Rule count SHOULD be 1")
        self.assertTrue(rule_key_exists, "Key 47|53 Should exist")

        instructions = get_printing_instructions()
        count = len(instructions)
        self.assertEqual(count, 1, "should have 1")

    def test_find_middle_value(self):
        value = "75,47,61,53,29"
        middle_value = find_middle_value(value)
        self.assertEqual(middle_value, 61, "Middle value SHOULD be 61")

    def test_validate_instructions(self):
        total = validate_instructions()
        self.assertEqual(total, 143, "how many")

if __name__ == "__main__":
    unittest.main(verbosity=2)
