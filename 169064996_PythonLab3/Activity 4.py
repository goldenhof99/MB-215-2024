is_true=True
is_false=False 
print("Logical Operations:")
print(f"is_true AND is_false: {is_true and is_false}") 
print(f"is_true OR is_false: {is_true or is_false}")  
print(f"NOT is_true: {not is_true}")                 
print(f"NOT is_false: {not is_false}")                 
print("\nConditional Statement Example:")
if is_true:
    print("The value of 'is_true' is True, so this block runs.")
else:
    print("The value of 'is_true' is False, so this block does not run.")
if is_false:
    print("The value of 'is_false' is True, so this block runs.")
else:
    print("The value of 'is_false' is False, so this block does not run.")

is_weekend = False 
if not is_weekend:
    print("It's a weekday. Time to go to school.")
else:
    print("It's the weekend. Enjoy this Sunday's football games!")

