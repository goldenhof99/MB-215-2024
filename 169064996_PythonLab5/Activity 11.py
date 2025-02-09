# Squaring each number in the list using list comprehension
list1 = [1, 2, 3, 4]
list2 = [item**2 for item in list1]  # List comprehension for squaring
print("Previous list:", list1)
print("New list with squared values:", list2)

# Getting the number of characters in each string in a list
str_list = ['Winken', 'Blinken', 'Nod']
len_list = [len(s) for s in str_list]  # List comprehension for length of each string
print("Number of chars in each string in the list:", len_list)

# Selective filtering: Keeping numbers < 10 using a for loop
list1 = [1, 12, 2, 20, 3, 15, 4]
list2 = [n for n in list1 if n < 10]  # List comprehension for filtering
print("List2 has all numbers that are less than 10:", list2)
