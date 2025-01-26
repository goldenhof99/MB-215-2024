print("Even numbers from 2 to 20:")
for num in range(2, 21, 2):  
    print(num, end=" ") 
print("\n")  

print("Multiplication table for numbers 1 to 3:")
for outer in range(1, 4): 
    row = ""  
    for inner in range(1, 11): 
        row += f"{outer} * {inner} = {outer * inner:<4}" 
        if inner % 7 == 0: 
            print(row.strip())  
            row = "" 
    if row:
        print(row.strip())
print()  

input_string = "Hello"
print(f"Reversing the string '{input_string}':")
for char in reversed(input_string):
    print(char, end=" ")  
print()  


