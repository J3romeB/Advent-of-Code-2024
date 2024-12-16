"""Solution for AoC 2024 day5 part 1"""
rule_dictionary = {}
printing_instructions = []

def get_rules():
    """global getter for rule_dictionary"""
    global rule_dictionary
    return rule_dictionary

def get_printing_instructions():
    """global getter for printing_instructions"""
    global printing_instructions
    return printing_instructions

def generate_printing_rules_and_instructions(file_name):
    """Generate the printing rules the update list must follow to be valid"""
    global rule_dictionary
    global printing_instructions

    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            temp_value = line.rstrip('\n')
            if "|" in temp_value:
                rule_dictionary[temp_value] = temp_value.split('|')
            elif "," in temp_value:
                printing_instructions.append(temp_value)

def find_middle_value(instruction):
    """Find the middle value to check for correctness"""
    list_of_strings = instruction.split(',')
    list_of_integers = [int(x) for x in list_of_strings]
    mid_index = int(len(list_of_integers)/2)
    return list_of_integers [mid_index]

def validate_instructions():
    """main function for validating printing instructions against update rules"""
    rules = get_rules()
    instructions = get_printing_instructions()
    total = 0

    for instruction in instructions:
        count = validate_current_instruction(rules, instruction)
        total = total + count
    return total

def validate_current_instruction(rules, instruction):
    """validates passed printing instruction against rule set and returns value of middle page"""
    pages = instruction.split(',')
    for i in range(0,len(pages)):
        for j in range(i+1,len(pages)):
            temp = pages[j]+'|'+pages[i]
            print(temp)
            if temp in rules:
                return 0
    return find_middle_value(instruction)

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
        distinct_path_traveled = simulate_guards_path(warehouse)
        self.assertEqual(distinct_path_traveled, 18, "these are not equal")


if __name__ == "__main__":
    unittest.main()