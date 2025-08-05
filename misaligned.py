
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    
    color_map = []  # List to store the color combinations
    
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            # Create a tuple for each combination and add it to the list
            color_map.append((major, minor))  # Store the tuple in the list
    
    # Print the color map
    for index, (major, minor) in enumerate(color_map):
        print(f'{index + 1} | {major} | {minor}')
    
    return color_map  # Return the list of color combinations

# Call the function and store the result
result = print_color_map()

# Assertions to validate the results
assert(len(result) == 25)  # Check if the total number of combinations is 25
assert(result[0] == ("White", "Blue"))  # Check the first combination
assert(result[1] == ("White", "Orange"))  # Check the second combination

print("All is well (maybe!)")




