# Demonstrates how to create and use immutable sets with frozenset().
languages = {"Python", "Java", "C++", "JavaScript"}

frozen_languages = frozenset(languages)

print("Original Set:")
print(languages)

print("\nFrozen Set:")
print(frozen_languages)

print("\n--- Bonus Challenge ---")

print(f"Type of languages: {type(languages)}")
print(f"Type of frozen_languages: {type(frozen_languages)}")

print("\n--- Extra Challenge ---")

try:
    frozen_languages.add("Go")
except AttributeError as e:
    print("Error:")
    print(e)