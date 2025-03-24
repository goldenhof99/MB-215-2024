def country_capital_directory():
    capitals = {
        "Canada": "Ottawa", "USA": "Washington, D.C.", "Japan": "Tokyo",
        "France": "Paris", "Brazil": "Brasília", "India": "New Delhi",
        "Germany": "Berlin", "Australia": "Canberra", "Mexico": "Mexico City",
        "Italy": "Rome"
    }

    while True:
        country = input("\nPlease enter a country to find its capital city (or type 'exit' to quit): ")
        if country.lower() == 'exit':
            break
        try:
            print(f"The capital city of {country} is {capitals[country]}.")
        except KeyError:
            print("Sorry, the country you are looking for is not in our directory.")

country_capital_directory()
