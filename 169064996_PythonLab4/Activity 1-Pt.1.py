import random  # Dice rolling generation

def roll_dice(num_dice, num_sides):
    """
    Simulates rolling a given number of dice with a specified number of sides.
    
    Parameters:
        num_dice (int): The number of dice to roll.
        num_sides (int): The number of sides on each die.
    
    Returns:
        int: The total sum of the dice rolls.
    """
    total = sum(random.randint(1, num_sides) for _ in range(num_dice))
    return total

# Testing the purpose of the code 
if __name__ == "__main__":
    print(f"Rolling 3 dice with 6 sides each: {roll_dice(3, 6)}")
