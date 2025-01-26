nGrade=float(input("Enter your numeric Grade:"))
if nGrade>=90: 
    lGrade="A+"
elif nGrade>=80:
    lGrade="A"
elif nGrade>=70:
    lGrade="B"
elif nGrade>=60:
    lGrade="C"
elif nGrade>=50:
    lGrade="D"
elif nGrade<=50:
    lGrade="F"
print(f"The letter grade for {nGrade} is a {lGrade}.")