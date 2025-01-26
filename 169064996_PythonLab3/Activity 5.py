total = 0
count = 0
while total < 100:
    user_input = input("Enter a number (or press space to exit): ").strip()
    if user_input == "":
        break
    try:
        number = float(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print(f"\nTotal sum: {total}")
print(f"Count of numbers entered: {count}")



