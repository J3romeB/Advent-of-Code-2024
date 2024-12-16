import math

count = 0
values_to_check = []
with open("day7\\test_input.txt", 'r', encoding='utf-8') as file:
    for line in file:
        values_to_check.append(line.rstrip('\n'))
#store as string

#loop over values
for value in values_to_check:
    #split on : to get value vs others
    equation = value.split(": ")
    answer_for_validation = int(equation[0])
    #split others on space to get individual integers (make them integers)

    numbers = [int(x) for x in equation[1].split(" ")]

    # Try adding all
    # Try multiply all
    # Try all the combos
    if sum(numbers) == answer_for_validation:
        count += answer_for_validation
    elif math.prod(numbers) == answer_for_validation:
        count += answer_for_validation
    else:
        pass
        




# If any equaled the vale add the value to count
