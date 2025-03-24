def count_before_m(s):
    return sum(1 for char in s.lower() if char.isalpha() and char < 'm')

def count_m_and_after(s):
    return sum(1 for char in s.lower() if char.isalpha() and char >= 'm')

def main():
    user_input = input("Please enter a string: ")
    print(f"\nNumber of letters before 'm' in the alphabet: {count_before_m(user_input)}")
    print(f"Number of letters 'm' or after in the alphabet: {count_m_and_after(user_input)}")

if __name__ == "__main__":
    main()
