# Demonstrates how to convert a list into a tuple using the tuple() function.
languages = ["Python", "Java", "C", "C++", "JavaScript"]

tuple_languages = tuple(languages)

print("Original List:")
print(languages)

print("\nConverted Tuple:")
print(tuple_languages)

print("\n--- Bonus Challenge ---")

print(f"Type of languages: {type(languages)}")
print(f"Type of tuple_languages: {type(tuple_languages)}")