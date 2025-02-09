# Define two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenating lists using the + operator (creates a new list)
concatenated_list = list1 + list2
print("Concatenated list using + operator:", concatenated_list)

# Concatenating lists using the += augmented assignment operator (modifies list1)
list1 = [1, 2, 3]  # Reset list1
list2 = [4, 5, 6]
list1 += list2  # This modifies list1 directly
print("Concatenated list using += operator:", list1)

# Attempting to concatenate a list with a number (this will cause an error)
list1 = [1, 2, 3]
number = 4

# Uncommenting the line below will result in a TypeError
# concatenated_list = list1 + number  
