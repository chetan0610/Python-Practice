# Demonstrates how to create sets efficiently using set comprehensions.
print("--- Challenge 1: Squares ---")
squares = {num ** 2 for num in range(1, 11)}
print("Squares:")
print(squares)

print("\n--- Bonus Challenge 1: Even Numbers ---")
even_numbers = {num for num in range(1, 21) if num % 2 == 0}
print("Even Numbers:")
print(even_numbers)

print("\n--- Bonus Challenge 2: First Letters ---")

languages = ["Python", "Java", "JavaScript", "C", "C++", "Go", "Ruby"]
first_letters = {lang[0] for lang in languages}
print("First Letters:")
print(first_letters)

print("\n--- Extra Challenge: Unique Words ---")
sentence = input("Enter a sentence:\n")

unique_words = {word.lower() for word in sentence.split()}

print("\nUnique Words:")
print(unique_words)