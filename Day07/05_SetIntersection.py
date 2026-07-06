# Demonstrates how to find common elements between two sets using intersection() and the '&' operator.
python_students = {"Rahul", "Priya", "Amit", "Sneha"}
java_students = {"Priya", "Sneha", "Kiran", "Vijay"}

print("Python Students:")
print(python_students)

print("\nJava Students:")
print(java_students)

print("\n--- Main Challenge ---")

common_students = python_students.intersection(java_students)
print("Common Students:")
print(common_students)

print("\n--- Bonus Challenge ---")

common_students_operator = python_students & java_students
print("Common Students using '&':")
print(common_students_operator)

print("\n--- Extra Challenge ---")

search_student = input("Enter student name: ")

if search_student in common_students:
    print(f"{search_student} is enrolled in both Python and Java.")
else:
    print(f"{search_student} is not enrolled in both courses.")