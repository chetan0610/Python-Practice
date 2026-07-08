# ==========================================
# Program 05: 05_LoopDictionary.py
# Description: Demonstrating how to loop through dictionary 
# keys, values, and items. Includes searching functionality.
# ==========================================
import json

# Reusable function to display the dictionary neatly
def display_dict(title, data_dict):
    print(f"\n========== {title} ==========")
    print(json.dumps(data_dict, indent=4))

def core_student_loops():
    """Handles Steps 2 through 7 from the objective."""
    student = {}
    print("--- Enter Student Details ---")
    
    # Step 2: Creating dictionary via user input
    try:
        student["id"] = int(input("ID: "))
        student["name"] = input("Name: ")
        student["course"] = input("Course: ")
        student["year"] = int(input("Year: "))
        student["college"] = input("College: ")
        student["phone"] = input("Phone: ")
        student["email"] = input("Email: ")
    except ValueError:
        print("Invalid input for ID or Year. Using default integers.")
        student["id"] = 0
        student["year"] = 1

    # Step 3: Display dictionary
    display_dict("STUDENT DICTIONARY", student)

    # Step 4: Loop through only keys
    print("\n========== KEYS ==========")
    for key in student.keys():
        print(key)

    # Step 5: Loop through only values
    print("\n========== VALUES ==========")
    for value in student.values():
        print(value)

    # Step 6: Loop through both keys and values
    print("\n========== KEY : VALUE ==========")
    for key, value in student.items():
        print(f"{key} : {value}")

    # Step 7: Count how many key-value pairs are present
    print(f"\nTotal Fields: {len(student)}")


def employee_bonus_and_extra():
    """Handles the Bonus Challenge (Employee Dict) and Extra Challenge (Search)."""
    print("\n" + "="*40)
    print("🎯 BONUS & 🔥 EXTRA CHALLENGE")
    print("="*40)
    
    # Bonus Challenge: Create an Employee Dictionary
    employee = {
        "employee_id": 9901,
        "name": "Jane Doe",
        "department": "Engineering",
        "salary": 85000,
        "experience": "5 Years"
    }

    display_dict("EMPLOYEE DICTIONARY", employee)

    print("\n--- Employee Keys ---")
    for key in employee.keys():
        print(key)

    print("\n--- Employee Values ---")
    for value in employee.values():
        print(value)

    print("\n--- Employee Key : Value ---")
    for key, value in employee.items():
        print(f"{key} : {value}")

    # Extra Challenge: Allow the user to search for a key
    print("\n--- Search for an Employee Key ---")
    search_key = input("Enter key to search (e.g., department, salary): ").strip().lower()
    
    if search_key in employee:
        print(f"{search_key} : {employee[search_key]}")
    else:
        print("Key not found!")

def main():
    # Run the core logic first
    core_student_loops()
    
    # Run the challenges
    employee_bonus_and_extra()
    
    print("\nProgram Completed Successfully! 🚀")

if __name__ == "__main__":
    main()