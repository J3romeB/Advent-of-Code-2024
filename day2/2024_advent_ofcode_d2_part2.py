# get input
# get parts
# check if passes increasing
# If yes mark safe, increase safe counter,  go to next line
# If no check if passes decreasing
# If yes mark safe, increase safe counter, go to next line
# return how many reports were safe
# Open the file for reading

import unittest
import os

here = os.path.dirname(os.path.abspath(__file__))

def is_increasing(numbers):
    """Function checking if numbers are increasing and within tolerance"""
    safe = False
    for i in range(len(numbers)-1):
        difference = numbers[i + 1] - numbers[i]
        if difference >= 1 and difference <= 3:
            safe = True
        else:
            return False
    return safe

def is_decreasing(numbers):
    """Function checking if numbers are decreasing and within tolerance"""
    safe = False
    for i in range(len(numbers)-1):
        difference = numbers[i] - numbers[i + 1]
        if difference >= 1 and difference <= 3:
            safe = True
        else:
            return False
    return safe

def is_safe(numbers):
    """Function checking if reports are safe"""
    #check if passes increase
    if is_increasing(numbers):
        return True
    elif is_decreasing(numbers):
        return True
    return False

def go_dirty(numbers):
    """Function that keeps trying removing values and trying"""
    #start manipulating the array to see if it will pass
    for i in range(len(numbers)):
        clone = numbers.copy()
        del clone[i]
        if is_safe(clone):
            return True
    print(numbers)
    return False

def count_safe_reports(file_name):
    """Function that opens a file of reports and counts how many of them are safe"""
    with open(file_name, "r", encoding="utf-8") as file:
        total_safe_reports = 0
        for line in file:
            # Strip the newline character and split by 4 spaces
            numbers = list(map(int, line.split()))
            if is_safe(numbers):
                total_safe_reports += 1
            elif go_dirty(numbers):
                total_safe_reports += 1

    return total_safe_reports

def is_safe_sequence(line):
    """Function that help unit testing a single line"""
    #Used for Unit Testing
    numbers = list(map(int, line.split()))
    if is_safe(numbers):
        return True
    elif go_dirty(numbers):
        return True
    return False


class TestIsSafeSequence(unittest.TestCase):
    def test_is_increasing(self):
        line = "1 3 6 7 9"
        numbers = list(map(int, line.split()))
        self.assertTrue(is_increasing(numbers))
    
    def test_is_decreasing(self):
        line = "7 6 4 2 1"
        numbers = list(map(int, line.split()))
        self.assertTrue(is_decreasing(numbers))

    def test_safe_sequence(self):
        self.assertTrue(is_safe_sequence("7 6 4 2 1"), "Should be safe, all numbers decrease by 1 or 2")
        self.assertTrue(is_safe_sequence("1 3 6 7 9"), "Should be safe, all numbers decrease by 1,2 or 3")
        self.assertTrue(is_safe_sequence("1 3 2 4 5"), "Safe by removing the second level, 3.")
        self.assertTrue(is_safe_sequence("8 6 4 4 1"), "Should be safe, same number twice removed")
        
    def test_not_safe_sequence(self):
        self.assertFalse(is_safe_sequence("1 2 7 8 9"), "Should not be safe, too big of an increase from 2 to 7")
        self.assertFalse(is_safe_sequence("9 7 6 2 1"), "Should not be safe, too big of a decrease from 6 to 2")
       

    def test_count_of_reports(self):
        file_name = os.path.join(here, 'day2-pt1-test.txt')
        safe_report_count = count_safe_reports(file_name)
        print(f"Total Safe Reports: {safe_report_count}")
        self.assertEqual(safe_report_count,4,"these are not equal")
    
    def test_count_of_reports_real(self):

        file_name = os.path.join(here, 'Values.txt')
        safe_report_count = count_safe_reports(file_name)
        #print(f"Total Safe Reports: {safe_report_count}")
        self.assertEqual(count_safe_reports(file_name),354,"these are not equal")
        

if __name__ == "__main__":
    unittest.main()