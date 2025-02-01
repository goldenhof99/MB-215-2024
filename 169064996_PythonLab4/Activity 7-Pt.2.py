import traceback  # Import for error handling

def append_to_file(filename, data):
    """
    Appends text to a file.

    Args:
        filename (str): File name.
        data (str): Text to append.
    """
    try:
        with open(filename, 'a') as file:
            file.write(data)
    except Exception:
        print(f"Error appending to file: {filename}")
        traceback.print_exc()

def read_from_file(filename):
    """
    Reads content from a file.

    Args:
        filename (str): File name.

    Returns:
        str: File content or None if an error occurs.
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except Exception:
        print(f"Error reading file: {filename}")
        traceback.print_exc()
        return None

# Test the code
if __name__ == "__main__":
    append_to_file('sample.txt', 'Adding more content.\n')
    
    # Make sure the code is defined before using it.
    content = read_from_file('sample.txt')  
    if content:
        print(f"Updated content of sample.txt:\n{content}")

