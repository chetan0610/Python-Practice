# Demonstrates how to find the number of elements in a set using len().
countries = {"India", "USA", "Japan", "Germany", "Australia"}
print("Countries:")
print(countries)

print(f"\nTotal Countries: {len(countries)}")

print("\n--- Bonus Challenge ---")

new_country = input("Enter a country: ")

if new_country not in countries:
    countries.add(new_country)
    print("\nUpdated Set:")
    print(countries)
else:
    print(f"\n{new_country} already exists in the set.")

print(f"\nTotal Countries: {len(countries)}")