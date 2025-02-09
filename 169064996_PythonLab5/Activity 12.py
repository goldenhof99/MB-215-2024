# Create a two-dimensional list (3x3 matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the two-dimensional list
print("Two-dimensional list (matrix):")
for row in matrix:
    print(row)  # Print each row of the matrix

# Accessing specific elements in the two-dimensional list
element_00 = matrix[0][0]  # First row, first column
element_12 = matrix[1][2]  # Second row, third column
element_21 = matrix[2][1]  # Third row, second column

print("\nAccessed elements:")
print(f"Element at [0][0]: {element_00}")
print(f"Element at [1][2]: {element_12}")
print(f"Element at [2][1]: {element_21}")

# Processing data in the two-dimensional list using nested loops
print("\nProcessed data (formatted matrix):")
for row in matrix:
    for element in row:
        print(element, end=' ')  # Print elements in the same row with spaces
    print()  # Print a newline after each row

