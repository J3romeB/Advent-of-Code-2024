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
    for i in enumerate(pages):
        for j in range(i+1,len(pages)):
            temp = pages[j]+'|'+pages[i]
            print(temp)
            if temp in rules:
                return 0
    return find_middle_value(instruction)
