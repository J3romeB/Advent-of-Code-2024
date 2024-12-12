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


def find_middle_value(pages):
    """Find the middle value to check for correctness"""
    mid_index = len(pages)//2
    return int(pages[mid_index])


def validate_instructions():
    """main function for validating printing instructions against update rules"""
    rules = get_rules()
    instructions = get_printing_instructions()
    total = 0

    for instruction in instructions:
        pages = instruction.split(',')
        is_valid, i, j = validate_current_instruction(rules, pages)
        if not is_valid:
            while True:
                print(f'instruction = {pages} i = {i} j= {j}')
                pages = swap_positons(pages, i, j)
                is_valid, i, j = validate_current_instruction(rules, pages)
                if is_valid:
                    total = total + find_middle_value(pages)
                    break
        else:
            #This was correct first time just pass
            pass
    return total


def swap_positons(pages, i, j):
    """takes a list and two positions you want to swap"""
    pages[i], pages[j] = pages[j], pages[i]
    return pages


def validate_current_instruction(rules, pages):
    """validates passed printing instruction against rule set and returns value of middle page"""
    for i in range(0, len(pages)):
        for j in range(i+1, len(pages)):
            temp = pages[j]+'|'+pages[i]
            if temp in rules:
                return False, i, j
    return True, i, j
