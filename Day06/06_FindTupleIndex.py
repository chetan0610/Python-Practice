# Demonstrates how to find the index of an element in a tuple using index().
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

print("Tuple:")
print(fruits)

print("\nIndex of Mango:", fruits.index("Mango"))
print("Index of Orange:", fruits.index("Orange"))

print("\n--- Bonus & Extra Challenge ---")

search_fruit = input("Enter a fruit to search: ")

try:
    fruit_index = fruits.index(search_fruit)
    print(f"{search_fruit} is found at index {fruit_index}.")
except ValueError:
    print(f"Sorry, '{search_fruit}' was not found in the tuple.")