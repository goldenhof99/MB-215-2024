import random

def exercise_selector():
    exercises = ["Plank", "Squat", "Sit-up", "Push-up"]
    while True:
        input("Tossing the pyramid... Press Enter to toss.")
        print(f"You should do: {random.choice(exercises)}")
        again = input("Would you like to toss again? (yes/no): ")
        if again.lower() != 'yes':
            break

exercise_selector()
