# Demonstrates how to add single and multiple elements to a set.
languages = {"Python", "Java", "C++"}

print("Original Set:")
print(languages)

languages.add("JavaScript")

languages.update(["Go", "Rust"])

print("\nSet after add() and update():")
print(languages)

print("\n--- Bonus Challenge ---")

new_language = input("Enter a language: ")

languages.add(new_language)

print("\nUpdated Set:")
print(languages)