import math

count = 0
values_to_check = []
with open("day7\\input.txt", 'r', encoding='utf-8') as file:
    for line in file:
        values_to_check.append(line.rstrip('\n'))

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
        continue_list = []
        for i, number in enumerate(numbers):
            if i == 0:
                continue_list.append(number)
            else:
                temp_list = []
                for i, current_item in enumerate(continue_list):
                    temp_add = current_item + number
                    temp_multi = current_item * number
                    temp_combo = int(str(current_item)+str(number))

                    if temp_add <= answer_for_validation:
                        temp_list.append(temp_add)
                
                    if temp_multi <= answer_for_validation:
                        temp_list.append(temp_multi)
                    
                    if temp_combo <= answer_for_validation:
                        temp_list.append(temp_combo)
                continue_list = temp_list.copy()

        if answer_for_validation in continue_list:
             count += answer_for_validation
            #check if we are still under the answer for validation for each of those
                #If under continue down that tree
                # for each of the values we have, 
                    #Add the next value and store it in a new spot,
                    #Multiply it by the next value and store it in a new spot
print(count)