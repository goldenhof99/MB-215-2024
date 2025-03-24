def calculate_ontario_tax(income):
    if income <= 40922:
        tax = income * 0.0505
    elif income <= 81847:
        tax = (income - 40922) * 0.0915 + 2067.00
    elif income <= 150000:
        tax = (income - 81847) * 0.1116 + 5811.00
    elif income <= 220000:
        tax = (income - 150000) * 0.1216 + 13417.00
    else:
        tax = (income - 220000) * 0.1316 + 21929.00
    return tax

def main():
    try:
        income = float(input("Enter your taxable income: $"))
        tax_paid = float(input("Enter the amount of tax already paid: $"))
        
        tax_owed = calculate_ontario_tax(income)
        balance = tax_owed - tax_paid

        print(f"\nOntario Tax Owed (Line 38): ${tax_owed:,.2f}")
        print(f"Remaining Tax Balance: ${balance:,.2f}")
        if balance < 0:
            print("You are entitled to a refund.")
        elif balance == 0:
            print("You have paid the correct amount of tax.")
        else:
            print("You still owe additional tax.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()
