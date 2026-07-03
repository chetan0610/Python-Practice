# Combines multiple tuple concepts to solve a practical problem.
students = (
    ("Rahul", 85),
    ("Priya", 92),
    ("Amit", 78),
    ("Sneha", 96),
    ("Kiran", 88)
)

print("Student Records\n")
for name, mark in students:
    print(f"{name} : {mark}")

print(f"\nTotal Students: {len(students)}")


marks_only = tuple(mark for name, mark in students)

print(f"\nHighest Marks: {max(marks_only)}")
print(f"Lowest Marks: {min(marks_only)}")

print("\n--- Bonus Challenge ---")

search_name = input("Enter student name: ")

student_found = False

for name, mark in students:
    if name.lower() == search_name.lower():
        print("\nStudent Found")
        print(f"Name  : {name}")
        print(f"Marks : {mark}")
        student_found = True
        break

if not student_found:
    print("\nStudent not found.")