import unittest
import os
import re
here = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(here, 'input.txt')
with open(file_name, "r") as file:
    text = file.read()
pattern = r"mul\((\d+),(\d+)\)"ccc
matches = re.findall(pattern, text)
total_sum = 0
for a, b in matches:
    total_sum += int(a) * int(b)
print(f"The total sum is: {total_sum}")

# class Test_day_3_solution(unittest.TestCase):
    
#     def test_is_increasing(self):


#     def test_count_of_reports(self):
#         file_name = "test-input.txt"
#         file_name = os.path.join(here, 'test-input.txt')
#         safe_report_count = count_safe_reports(file_name)
#         safe_report_count = count_safe_reports(file_name)
#         print(f"Total Safe Reports: {safe_report_count}")
#         self.assertEqual(count_safe_reports(file_name),2,"these are not equal")
    
# if __name__ == "__main__":
#     unittest.main()