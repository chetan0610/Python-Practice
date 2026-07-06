# Demonstrates how to find elements that exist in one set but not another using difference() and the '-' operator.
python_students = {"Rahul", "Priya", "Amit", "Sneha"}
java_students = {"Priya", "Sneha", "Kiran", "Vijay"}

print("Python Students:")
print(python_students)

print("\nJava Students:")
print(java_students)

print("\n--- Main Challenge ---")

python_only = python_students - java_students
print("Students only in Python:")
print(python_only)

print("\n--- Bonus Challenge ---")

java_only = java_students - python_students
print("Students only in Java:")
print(java_only)

print("\n--- Extra Challenge ---")

search_name = input("Enter student name: ")

if search_name in python_only:
    print(f"{search_name} is enrolled only in Python.")
elif search_name in java_only:
    print(f"{search_name} is enrolled only in Java.")
elif search_name in python_students and search_name in java_students:
    print(f"{search_name} is enrolled in both Python and Java.")
else:
    print(f"{search_name} is not enrolled in either course.")