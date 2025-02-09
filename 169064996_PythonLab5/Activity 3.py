# Define a list with numerical values
my_list = [10, 20, 30, 40, 50]

# Element to find in the list
element_to_find = 30

# Check if the element exists in the list
if element_to_find in my_list:
    index = my_list.index(element_to_find)  # Get the index of the element
    print(f"The element {element_to_find} is at index {index}.")
else:
    print(f"The element {element_to_find} is not in the list.")

# Print the value at a specific index (index 0)
print(f"The value at index 0 is {my_list[0]}.")

# Print the length of the list using len()
print(f"The length of the list is {len(my_list)}.")

# Change an element value in the list
my_list[0] = 999  # Updating the first element (index 0) to 999

# Print the new list after the change
print("The new list after the change is:", my_list)
