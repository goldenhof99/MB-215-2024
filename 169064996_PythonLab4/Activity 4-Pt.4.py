import random  # Import for generating interest rates

def simulate_investment(amount, years, rate_min, rate_max):
    """
    Simulates investment growth over time with varying interest rates.

    Args:
        amount (float): Initial investment amount.
        years (int): Duration in years.
        rate_min (float): Minimum possible annual interest rate.
        rate_max (float): Maximum possible annual interest rate.

    Returns:
        float: The final investment value after the given years.
    """
    for _ in range(years):
        rate = random.uniform(rate_min, rate_max) / 100  # Convert percentage to decimal
        amount += amount * rate  # Apply compound interest
    return amount

# Test the code
if __name__ == "__main__":
    final_amount = simulate_investment(1000, 5, 3, 7)
    print(f"Final investment value after 5 years: ${final_amount:.2f}")
