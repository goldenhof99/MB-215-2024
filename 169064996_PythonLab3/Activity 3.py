import math
diameter=float(input("Enter the diameter of the cylinder:"))
height=float(input("Enter the height of the cylinder:"))
pi=round(math.pi, 2)
radius=diameter/2
volume = pi * (radius ** 2) * height
print(f"The volume of the cylinder is {volume:.2f}.")