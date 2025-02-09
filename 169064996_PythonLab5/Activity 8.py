# Create a list with some initial elements
my_list = [10, 30, 20, 40, 20]
print("Initial list:", my_list)

# Append items to the list using the append() method
my_list.append(50)
my_list.append(20)  # Adding 20 again
print("The list after appending elements 50 & 20:", my_list)

# Insert an item at a specific index using the insert() method
my_list.insert(2, 25)  # Inserts 25 at index 2
print("The list after inserting 25 at index 2:", my_list)

# Sort the list using the sort() method (in-place)
my_list.sort()
print("The list after sorting:", my_list)

# Count the number of times an item appears in the list using the count() method
item_to_count = 20
count_result = my_list.count(item_to_count)
print(f"The item {item_to_count} appears {count_result} times in the list.")

# Find the index of the first occurrence of an item using the index() method
item_to_find = 20
try:
    index_result = my_list.index(item_to_find)
    print(f"The first occurrence of {item_to_find} is at index {index_result}.")
except ValueError:
    print(f"{item_to_find} is not in the list.")

# Remove an item from the list using the remove() method (removes the first occurrence)
item_to_remove = 20
my_list.remove(item_to_remove)
print("The list after removing 20:", my_list)

# Reverse the list using the reverse() method (in-place)
my_list.reverse()
print("The list after reversing:", my_list)

# Delete an item at a specific index using the del keyword
index_to_delete = 2
del my_list[index_to_delete]
print("The list after deleting item at index 2:", my_list)

# Calculate the sum of the elements in the list using the sum() function
list_sum = sum(my_list)

# Find the minimum and maximum values in the list using the min() and max() functions
list_min = min(my_list)
list_max = max(my_list)

# Print the updated list and the results of sum, min, and max
print("Updated list:", my_list)
print(f"Sum of elements: {list_sum}")
print(f"Minimum value: {list_min}")
print(f"Maximum value: {list_max}")
