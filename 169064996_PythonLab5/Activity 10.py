# Function to save a list to a file
def save_list_to_file(file_name, input_list):
    """Writes each item of the list to a new line in the file."""
    with open(file_name, 'w') as file:
        file.writelines(f"{item}\n" for item in input_list)

# Function to read data from a file and return it as a list
def read_list_from_file(file_name):
    """Reads data from a file and returns it as a list of strings."""
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]  # Remove leading/trailing spaces
    except FileNotFoundError:
        print("Error: File not found.")
        return []

# Original list
original_list = ['Apple', 'Banana', 'Cherry', 'Date']

# File name to save and read data
file_name = 'fruits.txt'

# Save the list to a file
save_list_to_file(file_name, original_list)
print(f"List saved to {file_name}")

# Read data from the file
read_data = read_list_from_file(file_name)

# Print the read data
print("Data read from the file:", read_data)
