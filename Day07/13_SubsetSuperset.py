# Demonstrates how to check subset and superset relationships between sets.
python_basics = {"Variables", "Loops", "Functions"}
python_course = {"Variables", "Loops", "Functions", "Lists", "Tuples", "Sets"}

print("Python Basics:")
print(python_basics)

print("\nPython Course:")
print(python_course)

is_subset = python_basics.issubset(python_course)
print(f"\nIs Python Basics a subset of Python Course? {is_subset}")

is_superset = python_course.issuperset(python_basics)
print(f"Is Python Course a superset of Python Basics? {is_superset}")

print("\n--- Bonus Challenge ---")

print(f"Using '<=' (subset): {python_basics <= python_course}")
print(f"Using '>=' (superset): {python_course >= python_basics}")

print("\n--- Extra Challenge ---")

advanced_topics = {"OOP", "File Handling"}

print(f"Is Advanced Topics a subset? {advanced_topics.issubset(python_course)}")