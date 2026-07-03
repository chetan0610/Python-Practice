# Demonstrates how to repeat tuple elements using the '*' operator.
days = ("Mon", "Tue", "Wed")

repeated_days = days * 3

print("Original Tuple:")
print(days)

print("\nRepeated Tuple:")
print(repeated_days)

print("\n--- Bonus Challenge ---")

repetitions = int(input("Enter the number of repetitions: "))

user_repeated_days = days * repetitions

print("\nRepeated Tuple:")
print(user_repeated_days)