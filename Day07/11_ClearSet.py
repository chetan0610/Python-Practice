# Demonstrates how to remove all elements from a set using the clear() method.
books = {"Python", "Java", "C++", "JavaScript", "Go"}

print("Original Set:")
print(books)

books.clear()

print("\nAfter clear():")
print(books)

is_empty = len(books) == 0
print(f"\nIs the set empty? {is_empty}")

print("\n--------------------------\n")

print("--- Extra Challenge ---")

books = {"Python", "Java", "C++", "JavaScript", "Go"}

choice = input("Do you want to clear the set? (yes/no): ").strip().lower()

if choice == 'yes':
    books.clear()
    print("\nSet has been cleared.")
    print(books)
else:
    print("\nSet was not cleared.")
    print(books)