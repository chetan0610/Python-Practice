# Demonstrates how to count occurrences of elements in a tuple using count().
numbers = (10, 20, 30, 20, 40, 20, 50, 10)

print("Tuple:")
print(numbers)

print("\nCount of 20:", numbers.count(20))
print("Count of 10:", numbers.count(10))
print("Count of 100:", numbers.count(100))

print("\n--- Bonus Challenge ---")

search_num = int(input("Enter a number to search: "))

appearances = numbers.count(search_num)
print(f"{search_num} appears {appearances} time(s) in the tuple.")