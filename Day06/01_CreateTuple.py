# Demonstrates how to create tuples and explains tuple immutability.
numbers = (10, 20, 30, 40, 50)
fruits = ("Apple", "Banana", "Mango", "Orange")

fruits_list = ["Apple", "Banana", "Mango", "Orange"]

print("Numbers:", numbers)
print("Fruits:", fruits)
print(type(numbers))
print(type(fruits))

print("\n--- The Big Difference: Immutability ---")

fruits_list[0] = "Strawberry"
print("Modified Fruits List:", fruits_list)