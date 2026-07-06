# Demonstrates how to check whether an element exists in a set using 'in' and 'not in'.
courses = {"Python", "Java", "C++", "JavaScript", "Go"}

print("Available Courses:")
print(courses)

print("\n--- Main Challenge ---")

print(f"Is Python available? {'Python' in courses}")
print(f"Is Rust available? {'Rust' in courses}")

print("\n--- Extra Challenge ---")

print(f"Is Swift not available? {'Swift' not in courses}")

print("\n--- Bonus Challenge ---")

search_course = input("Enter a course: ")

if search_course in courses:
    print(f"\n{search_course} is available.")
else:
    print(f"\n{search_course} is not available.")