# Demonstrates how to remove duplicate elements from a list by converting it into a set.
numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60]

print("Original List:")
print(numbers)

unique_numbers = set(numbers)

print("\nUnique Elements:")
print(unique_numbers)

print("\n--- Bonus Challenge ---")

unique_list = list(unique_numbers)

print("Unique List:")
print(unique_list)

print("\n--- Extra Challenge ---")

user_numbers = list(map(int, input("Enter numbers separated by spaces:\n").split()))

print("\nOriginal List:")
print(user_numbers)

print("\nUnique Elements:")
print(set(user_numbers))