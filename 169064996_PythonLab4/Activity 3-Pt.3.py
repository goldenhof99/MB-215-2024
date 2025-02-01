import random  # Import for generating random numbers

def generate_random_number(min_val, max_val):
    """
    Generates a random number between given min and max values.

    Args:
        min_val (int): Minimum possible value.
        max_val (int): Maximum possible value.

    Returns:
        int: A random integer between min_val and max_val.
    """
    return random.randint(min_val, max_val)

# Test the code
if __name__ == "__main__":
    random_number = generate_random_number(1, 100)
    print(f"The generated random number is: {random_number}")
