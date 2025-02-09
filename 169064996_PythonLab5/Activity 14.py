# Create a tuple with a list as its third element
t = (10, 20, [97, 98, 99])

# Convert the tuple to a list using list()
list_from_tuple = list(t)

# Print the list obtained from the tuple
print("List from tuple:", list_from_tuple)

# Modify the list (now it's a list, so we can modify it)
list_from_tuple[2].append(100)  # Add an element to the nested list

# Convert the modified list back to a tuple using tuple()
tuple_from_list = tuple(list_from_tuple)

# Print the final tuple
print("Tuple from modified list:", tuple_from_list)
