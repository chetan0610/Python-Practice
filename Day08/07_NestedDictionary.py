# ==========================================
# Program 07: 07_NestedDictionary.py
# Description: Demonstrating nested dictionaries
# with add, view, search, and update functionality.
# ==========================================
import json

def display_students(title, student_data):
    print(f"\n========== {title} ==========")
    print(json.dumps(student_data, indent=4))

def main():
    # Core & Bonus Challenge: Nested Dictionary with Phone and Email
    students = {
        101: {
            "name": "Aarav",
            "course": "Computer Science",
            "marks": 92.5,
            "phone": "9876543210",
            "email": "aarav@gmail.com"
        },
        102: {
            "name": "Priya",
            "course": "Electronics",
            "marks": 88.0,
            "phone": "9123456789",
            "email": "priya@gmail.com"
        }
    }

    while True:
        print("\n" + "="*35)
        print("🎓 STUDENT DATABASE MANAGER")
        print("="*35)
        print("1. Add a Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student Marks")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ").strip()

        if choice == '1':
            print("\n--- Add New Student ---")
            try:
                # Using int() for ID so it acts as a proper dictionary key
                student_id = int(input("Enter Student ID: "))
                
                if student_id in students:
                    print("Error: Student ID already exists!")
                else:
                    name = input("Name: ")
                    course = input("Course: ")
                    marks = float(input("Marks: "))
                    phone = input("Phone: ")
                    email = input("Email: ")
                    
                    # Creating the nested dictionary inside the main dictionary
                    students[student_id] = {
                        "name": name,
                        "course": course,
                        "marks": marks,
                        "phone": phone,
                        "email": email
                    }
                    print(f"\n✅ Student '{name}' added successfully!")
            except ValueError:
                print("❌ Invalid input! ID and Marks must be numbers.")

        elif choice == '2':
            if students:
                display_students("ALL REGISTERED STUDENTS", students)
            else:
                print("\nNo students found in the database.")

        elif choice == '3':
            try:
                search_id = int(input("\nEnter Student ID to search: "))
                if search_id in students:
                    display_students(f"STUDENT RECORD: {search_id}", students[search_id])
                else:
                    print("\n❌ Student not found!")
            except ValueError:
                print("❌ Invalid input! ID must be a number.")

        elif choice == '4':
            # Extra Challenge: Update a student's marks
            try:
                update_id = int(input("\nEnter Student ID to update marks: "))
                if update_id in students:
                    current_marks = students[update_id]['marks']
                    print(f"Current Marks for {students[update_id]['name']}: {current_marks}")
                    
                    new_marks = float(input("Enter New Marks: "))
                    students[update_id]['marks'] = new_marks
                    print("\n✅ Marks updated successfully!")
                else:
                    print("\n❌ Student not found!")
            except ValueError:
                print("❌ Invalid input! ID and Marks must be numbers.")

        elif choice == '5':
            print("\nExiting Database Manager. Have a great day! 🚀")
            break

        else:
            print("\n❌ Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()