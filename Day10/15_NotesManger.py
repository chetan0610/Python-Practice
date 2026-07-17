"""
15_NotesManager.py
Student Record Manager covering complete CRUD operations via functions.
"""
import json
import os

FILE_NAME = "students_db.json"

def load_data():
    """Loads student data from JSON."""
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except Exception:
        return {}

def save_data(data):
    """Saves student data to JSON."""
    try:
        with open(FILE_NAME, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Save error: {e}")

def add_student(data):
    """Adds a new student to the dictionary."""
    roll = input("Enter Roll Number: ").strip()
    name = input("Enter Name: ").strip()
    data[roll] = name
    save_data(data)
    print("Student added.")

def view_students(data):
    """Displays all students."""
    if not data:
        print("No students found.")
        return
    for roll, name in data.items():
        print(f"Roll: {roll} | Name: {name}")

def search_student(data):
    """Searches for a student by roll number."""
    roll = input("Enter Roll Number to search: ").strip()
    if roll in data:
        print(f"Found: {data[roll]}")
    else:
        print("Student not found.")

def delete_student(data):
    """Removes a student from the database."""
    roll = input("Enter Roll Number to delete: ").strip()
    if roll in data:
        del data[roll]
        save_data(data)
        print("Student deleted.")
    else:
        print("Student not found.")

def main():
    """Main loop for the Student Record Manager."""
    data = load_data()
    while True:
        print("\n1. Add | 2. View | 3. Search | 4. Delete | 5. Exit")
        choice = input("Choice: ").strip()
        if choice == '1': add_student(data)
        elif choice == '2': view_students(data)
        elif choice == '3': search_student(data)
        elif choice == '4': delete_student(data)
        elif choice == '5': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()