# Demonstrates how to find the smallest element in a tuple using min().
temperatures = (32, 28, 35, 30, 26, 31)

print("Temperatures:")
print(temperatures)

lowest_temp = min(temperatures)
print(f"\nLowest Temperature: {lowest_temp}")

print("\n--- Bonus Challenge ---")

user_temp = int(input("Enter a temperature: "))

if user_temp == lowest_temp:
    print(f"{user_temp} is the lowest temperature.")
else:
    print(f"{user_temp} is not the lowest temperature.")