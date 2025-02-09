# Define a list with 10 elements
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic list slicing (elements from index 2 to 5)
basic_slice = my_list[2:6]  # [2, 3, 4, 5]
print("Basic slice:", basic_slice)

# Slicing from the beginning (start not specified, default is 0)
start_not_specified = my_list[:4]  # [0, 1, 2, 3]
print("Slice with start not specified:", start_not_specified)

# Slicing until the end (end not specified, default is length of list)
end_not_specified = my_list[7:]  # [7, 8, 9]
print("Slice with end not specified:", end_not_specified)

# Slicing with a step value (every 2nd element from index 1 to 7)
step_slice = my_list[1:8:2]  # [1, 3, 5, 7]
print("Slice with step value:", step_slice)

# Slicing using negative indexes (last 4 elements, excluding the last one)
negative_indexes = my_list[-5:-1]  # [5, 6, 7, 8]
print("Slice with negative indexes:", negative_indexes)