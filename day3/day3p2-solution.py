import unittest
import os
import re

here = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(here, 'p2test-input.txt')
file_name = os.path.join(here, 'input.txt')

# Read the content of the file into the text variable
with open(file_name, "r") as file:
    text = file.read()

# Regular expression to capture digits from valid 'mul(...)'
# pattern = r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)"
pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"

# Find all matches
matches = re.findall(pattern, text)
print(f"Matches found: {matches}")

# Initialize total sum
total_sum = 0


def do_math(extract_me):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, extract_me)
    for a, b in matches:
        return int(a) * int(b)


enabled = True
for value in matches:
    if enabled:
        if value == "don't()":
            enabled = False
        elif value == "do()":
            enabled = True
        else:
            total_sum += do_math(value)
    else:
        if value == "don't()":
            enabled = False
        elif value == "do()":
            enabled = True

print(f"Total sum {total_sum}")

class Test_day_3_solution(unittest.TestCase):

    def test_line(self):
        total = 0
        test_list = ['mul(2,4)', "don't()", 'mul(5,5)',
                     'mul(11,8)', 'do()', 'mul(8,5)']
        enabled = True
        for value in test_list:
            if enabled:
                if value == "don't()":
                    enabled = False
                elif value == "do()":
                    enabled = True
                else:
                    total += do_math(value)
            else:
                if value == "don't()":
                    enabled = False
                elif value == "do()":
                    enabled = True
        self.assertEqual(total, 48, "these are not equal")


if __name__ == "__main__":
    unittest.main()
