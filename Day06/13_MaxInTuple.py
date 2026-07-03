# Demonstrates how to find the largest element in a tuple using max().
marks = (85, 92, 78, 96, 88, 90)

print("Marks:")
print(marks)

highest_mark = max(marks)
print(f"\nHighest Marks: {highest_mark}")

print("\n--- Bonus Challenge ---")

user_mark = int(input("Enter a mark: "))

if user_mark == highest_mark:
    print(f"{user_mark} is the highest mark.")
else:
    print(f"{user_mark} is not the highest mark.")