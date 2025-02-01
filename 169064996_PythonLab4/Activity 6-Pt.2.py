import traceback  # Import for error handling 

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
    content = read_from_file('sample.txt')
    if content:
        print(f"Content of sample.txt:\n{content}")
