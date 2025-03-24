def recipe_tracker():
    recipes = []

    while True:
        print("\nWelcome to the Recipe Ingredients Tracker!")
        print("1 - Add a New Recipe")
        print("2 - View a Recipe")
        print("3 - List All Recipes")
        print("4 - Remove a Recipe")
        print("0 - Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the recipe name: ")
            ingredients = input("Enter the ingredients (separated by commas): ").split(",")
            recipes.append((name, [i.strip() for i in ingredients]))
            print(f"Recipe '{name}' added successfully!")
        elif choice == '2':
            search = input("Which recipe would you like to view? ")
            for r in recipes:
                if r[0].lower() == search.lower():
                    print(f"\nIngredients for '{r[0]}':")
                    for i in r[1]:
                        print(f"- {i}")
                    break
            else:
                print("Recipe not found.")
        elif choice == '3':
            print("\nAll Recipes:")
            for i, r in enumerate(recipes, 1):
                print(f"{i}. {r[0]}")
        elif choice == '4':
            to_remove = input("Enter the recipe name to remove: ")
            for r in recipes:
                if r[0].lower() == to_remove.lower():
                    recipes.remove(r)
                    print("Recipe removed.")
                    break
            else:
                print("Recipe not found.")
        elif choice == '0':
            print("Thank you for using the Recipe Ingredients Tracker. Goodbye!")
            break
        else:
            print("Invalid option.")

recipe_tracker()
