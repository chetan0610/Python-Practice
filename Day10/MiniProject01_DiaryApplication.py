"""
MiniProject01_DiaryApplication.py
Notes Manager: Add, View, Delete, and Save notes.
"""
import os

FILE_NAME = "my_notes.txt"

def display_menu():
    """Prints the application menu."""
    print("\n--- Notes Manager ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete All Notes")
    print("4. Exit")

def add_note():
    """Appends a new note to the file."""
    note = input("Enter your note: ")
    try:
        with open(FILE_NAME, 'a', encoding='utf-8') as file:
            file.write(note + '\n')
        print("Note saved.")
    except Exception as e:
        print(f"Error saving note: {e}")

def view_notes():
    """Reads and displays all notes."""
    try:
        if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
            print("No notes available.")
            return
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            for i, note in enumerate(file, 1):
                print(f"{i}. {note.strip()}")
    except Exception as e:
        print(f"Error reading notes: {e}")

def delete_notes():
    """Deletes the notes file."""
    confirm = input("Are you sure you want to delete all notes? (y/n): ").lower()
    if confirm == 'y':
        try:
            if os.path.exists(FILE_NAME):
                os.remove(FILE_NAME)
                print("All notes deleted.")
            else:
                print("No notes to delete.")
        except Exception as e:
            print(f"Error deleting notes: {e}")

def main():
    """Main loop for Notes Manager."""
    while True:
        display_menu()
        choice = input("Select an option: ").strip()
        if choice == '1': add_note()
        elif choice == '2': view_notes()
        elif choice == '3': delete_notes()
        elif choice == '4': break
        else: print("Invalid option.")

if __name__ == "__main__":
    main()