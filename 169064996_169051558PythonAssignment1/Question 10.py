import turtle

def draw_square(length, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)
    turtle.end_fill()

def draw_triangle(length, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)
    turtle.end_fill()

def draw_circle(radius, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(width, height, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def shape_drawer():
    print("Welcome to the Turtle Geometric Shapes Drawing Program!")
    while True:
        print("\nSelect the shape to draw:")
        print("1 - Square\n2 - Triangle\n3 - Circle\n4 - Rectangle\n0 - Exit")
        choice = input("Enter your choice: ")

        if choice == '0':
            break

        color = input("Enter the color: ")

        if choice == '1':
            side = int(input("Enter the side length: "))
            draw_square(side, color)
        elif choice == '2':
            side = int(input("Enter the side length: "))
            draw_triangle(side, color)
        elif choice == '3':
            radius = int(input("Enter the radius: "))
            draw_circle(radius, color)
        elif choice == '4':
            width = int(input("Enter the width: "))
            height = int(input("Enter the height: "))
            draw_rectangle(width, height, color)
        else:
            print("Invalid choice.")

        again = input("Would you like to draw another shape (yes/no)? ")
        if again.lower() != 'yes':
            break

    turtle.done()

shape_drawer()
