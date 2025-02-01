import traceback  # Import for error handling

def write_to_file(filename, data):
    """
    Writes data to a specified file.

    Args:
        filename (str): The name of the file to write to.
        data (str): The content to write into the file.
    """
    try:
        with open(filename, 'w') as file:  # Open file in write mode
            file.write(data)  # Write data to the file
    except Exception:
        print(f"Error writing to file: {filename}")
        traceback.print_exc()  # Print error message

# Test the code
if __name__ == "__main__":
    write_to_file('sample.txt', 'Hello, World!\n')  # Writing a sample text
    print("Data successfully written to sample.txt")

