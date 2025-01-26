km_to_miles_factor = 0.621371
distance_km = float(input("Enter distance in kilometers: "))
distance_miles = distance_km * km_to_miles_factor
distance_miles_rounded = round(distance_miles, 2)
print(f"{distance_km} kilometers is equal to {distance_miles_rounded} miles.")
