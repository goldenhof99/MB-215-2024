import turtle
ITERATIONS = 50
ANGLE = 25
SIZE = 120 
screen = turtle.Screen()
screen.bgcolor("black") 
screen.title("Geometric Art - Spiral of Squares")  
pattern_turtle = turtle.Turtle()
pattern_turtle.speed(0)  
pattern_turtle.pensize(2)  
colors = ["red", "orange", "yellow", "green", "blue", "purple","pink"]
for i in range(ITERATIONS):
    pattern_turtle.pencolor(colors[i % len(colors)]) 
    for _ in range(4):
        pattern_turtle.forward(SIZE)
        pattern_turtle.right(90)  
    pattern_turtle.right(ANGLE)
turtle.done()
