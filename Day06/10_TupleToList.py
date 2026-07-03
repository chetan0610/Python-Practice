# Demonstrates how to convert a tuple into a list using the list() function.
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

fruits_list = list(fruits)

print("Original Tuple:")
print(fruits)

print("\nConverted List:")
print(fruits_list)

print("\n--- Bonus Challenge ---")

fruits_list.append("Pineapple")

print("Updated List:")
print(fruits_list)

print(f"\nType of fruits: {type(fruits)}")
print(f"Type of fruits_list: {type(fruits_list)}")