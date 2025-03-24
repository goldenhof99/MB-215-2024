import math

def are_balls_touching(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    touching = distance <= (r1 + r2)
    return distance, touching

def main():
    try:
        # Input for ball 1
        x1 = float(input("Enter x-coordinate for ball 1: "))
        y1 = float(input("Enter y-coordinate for ball 1: "))
        r1 = float(input("Enter radius for ball 1: "))

        # Input for ball 2
        x2 = float(input("Enter x-coordinate for ball 2: "))
        y2 = float(input("Enter y-coordinate for ball 2: "))
        r2 = float(input("Enter radius for ball 2: "))

        # Output inputs
        print(f"\nBall 1: Center = ({x1}, {y1}), Radius = {r1}")
        print(f"Ball 2: Center = ({x2}, {y2}), Radius = {r2}")

        # Calculate distance and check if touching
        distance, touching = are_balls_touching(x1, y1, r1, x2, y2, r2)
        print(f"Distance between centers: {distance}")

        # Output result
        if touching:
            print("Result: The balls are touching.")
        else:
            print("Result: The balls are not touching.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
