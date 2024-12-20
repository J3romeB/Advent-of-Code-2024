dict_map = {}
def get_the_coordinates_for_current_tower_antinode(origin_tower, other_tower):
        y1 = coordinate[0]
        y2 = next_coordinate[0]
        x1 = coordinate[1]
        x2 = coordinate[1]

with open("day8\\test_input.txt", 'r', encoding='utf-8') as file:
    for row, line in enumerate(file):
        for column, alpha in enumerate(line.rstrip('\n')):
            if alpha != '.':
                #Check if alpha has an entry in dict_map, if it does add the x,y coordinates from row and col as a set
                if alpha in dict_map:
                    dict_map[alpha].add((row,column))
                else:
                    dict_map[alpha] = {(row,column)}

for ant_type in dict_map:
    coordinate_list = dict_map[ant_type]
    for i,coordinate in enumerate(coordinate_list):
        #loop over everything and ignore my self
        next_coordinate = coordinate_list[i+1]
        anti_tower_coordiantes = get_the_coordinates_for_current_tower_antinode(coordinate,next_coordinate)
        #get me the distance AND direction
        pass
print(dict_map)
    # Look for Antennes on the line
    # Add all coordinates for a specific Antenna letter into a dict
    # loop over the dict and go character by character
    # Skip navigation
    # the dict and see if you could place an antinode (inside boundry)
    # placing antinode is find the distance between the two antenaa in X Y and add that in the opposite directions
    # if yes, add that coordinate to somethin that doesn't allow duplicates
    # at the end check for all the antinodes