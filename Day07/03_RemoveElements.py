# Demonstrates how to remove elements from a set using remove(), discard(), and pop().
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}

print("Original Set:")
print(fruits)
print("\n--- Step 1: remove() ---")

fruits.remove("Banana")
print("Updated Set:")
print(fruits)

print("\n--- Step 2: discard() ---")

fruits.discard("Orange")
print("Updated Set:")
print(fruits)

print("\n--- Step 3: pop() ---")
removed_fruit = fruits.pop()
print("Randomly Removed Element:")
print(removed_fruit)

print("\nSet after pop():")
print(fruits)

print("\n--- Bonus Challenge ---")
user_fruit = input("Enter a fruit to remove: ")

initial_length = len(fruits)

fruits.discard(user_fruit)

if len(fruits) == initial_length:
    print("\nFruit not found (or no changes made).")

print("\nUpdated Set:")
print(fruits)