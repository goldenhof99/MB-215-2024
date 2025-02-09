# Original list
original_list = [1, 2, 3, 4, 5]

# Method 1: Using a for loop to create a copy
copied_list1 = []
for item in original_list:
    copied_list1.append(item)

# Print the copied list
print("Method 1: Copied list using a for loop:", copied_list1)

# Method 2: Concatenating the old list to create a copy
copied_list2 = [] + original_list

# Print the copied list
print("Method 2: Copied list using concatenation:", copied_list2)

# Method 3: Using the list() function to create a copy
copied_list3 = list(original_list)

# Print the copied list
print("Method 3: Copied list using list() constructor:", copied_list3)

# Perform calculations on the copied list

# Calculate the total of numeric values in the copied list
total = sum(copied_list3)

# Calculate the average of numeric values in the copied list
average = total / len(copied_list3) if copied_list3 else 0

# Print the total and average
print("Total of numeric values in the copied list:", total)
print("Average of numeric values in the copied list:", average)
