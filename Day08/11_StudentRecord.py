# ==========================================
# Program 11: 11_StudentRecord.py
# Description: Mini Project - Student Record Management System
# Features: Add, View, Search, Update, Delete, Average, and Topper
# ==========================================

def main():
    # Initialize with some dummy data for quick testing
    students = {
        101: {"name": "Chetan", "marks": 95},
        102: {"name": "Priya", "marks": 88},
        103: {"name": "Aarav", "marks": 92}
    }

    while True:
        print("\n" + "="*40)
        print("🎓 STUDENT RECORD MANAGEMENT SYSTEM 🎓")
        print("="*40)
        print("1. Add Student")
        print("2. View All Students & Average Marks")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. View Class Topper")
        print("7. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            print("\n--- Add New Student ---")
            try:
                stu_id = int(input("Enter Student ID: "))
                if stu_id in students:
                    print("❌ Error: Student ID already exists!")
                else:
                    name = input("Enter Student Name: ").title()
                    marks = float(input("Enter Marks: "))
                    students[stu_id] = {"name": name, "marks": marks}
                    print(f"✅ Student {name} added successfully!")
            except ValueError:
                print("❌ Invalid input! ID and Marks must be numbers.")

        elif choice == '2':
            print("\n--- All Students ---")
            if not students:
                print("No records found.")
            else:
                total_marks = 0
                print(f"{'ID':<10} | {'NAME':<15} | {'MARKS'}")
                print("-" * 40)
                for stu_id, info in students.items():
                    print(f"{stu_id:<10} | {info['name']:<15} | {info['marks']}")
                    total_marks += info['marks']
                
                # Bonus Challenge: Calculate Average Marks
                average = total_marks / len(students)
                print("-" * 40)
                print(f"Total Students: {len(students)}")
                print(f"Class Average: {average:.2f}")

        elif choice == '3':
            print("\n--- Search Student ---")
            try:
                stu_id = int(input("Enter Student ID to search: "))
                if stu_id in students:
                    info = students[stu_id]
                    print(f"✅ Found: ID: {stu_id} | Name: {info['name']} | Marks: {info['marks']}")
                else:
                    print("❌ Student not found.")
            except ValueError:
                print("❌ Invalid input! ID must be a number.")

        elif choice == '4':
            print("\n--- Update Student ---")
            try:
                stu_id = int(input("Enter Student ID to update: "))
                if stu_id in students:
                    print(f"Current Marks for {students[stu_id]['name']}: {students[stu_id]['marks']}")
                    new_marks = float(input("Enter New Marks: "))
                    students[stu_id]['marks'] = new_marks
                    print("✅ Marks updated successfully!")
                else:
                    print("❌ Student not found.")
            except ValueError:
                print("❌ Invalid input! ID and Marks must be numbers.")

        elif choice == '5':
            print("\n--- Delete Student ---")
            try:
                stu_id = int(input("Enter Student ID to delete: "))
                if stu_id in students:
                    removed = students.pop(stu_id)
                    print(f"✅ Student {removed['name']} deleted successfully!")
                else:
                    print("❌ Student not found.")
            except ValueError:
                print("❌ Invalid input! ID must be a number.")

        elif choice == '6':
            # Extra Challenge: Display Topper
            print("\n--- Class Topper ---")
            if not students:
                print("No records found.")
            else:
                # Find the student ID with the maximum marks
                topper_id = max(students, key=lambda x: students[x]['marks'])
                topper_info = students[topper_id]
                print("🏆 🥇 TOPPER 🥇 🏆")
                print(f"ID: {topper_id}")
                print(f"Name: {topper_info['name']}")
                print(f"Marks: {topper_info['marks']}")

        elif choice == '7':
            print("\nExiting Student Record Management System. Goodbye! 🚀")
            break

        else:
            print("❌ Invalid choice. Please select a number from 1 to 7.")

if __name__ == "__main__":
    main()