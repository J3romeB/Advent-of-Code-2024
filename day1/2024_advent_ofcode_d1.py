# get input
# split into to arrays by delimiter
# sort array 1 smallest to largest
# sort array 2 smallest to largest
# iterate over arrays and get the difference
# add the difference to total
# return total

# Open the file for reading
with open("advent_of_code_input_day_1.txt", "r", encoding="utf-8") as file:
    total_difference = 0
    left_list = []
    right_list = []
    for line in file:
        # Strip the newline character and split by 4 spaces
        parts = line.strip().split("   ")
        if len(parts) == 2:  # Ensure the line has exactly two parts
            num_1 = int(parts[0])  # Convert the first number to an integer
            num_2 = int(parts[1])  # Convert the second number to an integer
            left_list.append(num_1)
            right_list.append(num_2)
            
            # Example usage
            #print(f"num_1: {num_1}, num_2: {num_2}")
    left_list.sort()
    right_list.sort()
# Calculate the absolute differences
differences = []
for left, right in zip(left_list, right_list):
    differences.append(abs(left - right))

# Calculate the total difference
total_difference = sum(differences)

# Print the results
print(f"Total Difference: {total_difference}")
