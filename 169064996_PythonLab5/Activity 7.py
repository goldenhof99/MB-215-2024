# Create an empty list
my_list = []

# Append items to the list using the append() method
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(20)  # Adding the same item multiple times

# Print the current list
print("Current list:", my_list)

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

# Attempt to find the index of an item not in the list (raises ValueError)
item_not_in_list = 40
try:
    index_result = my_list.index(item_not_in_list)
    print(f"The first occurrence of {item_not_in_list} is at index {index_result}.")
except ValueError:
    print(f"{item_not_in_list} is not in the list, and it raises a ValueError.")
