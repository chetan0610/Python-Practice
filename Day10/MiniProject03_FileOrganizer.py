"""
MiniProject03_FileOrganizer.py
Diary Application: Password Protection, Add, View, and Search entries.
"""
import os
from datetime import datetime

FILE_NAME = "diary.txt"
PASSWORD = "admin"  # In a real app, hash this!

def authenticate():
    """Prompts for a password to protect entries."""
    attempts = 3
    while attempts > 0:
        pwd = input("Enter Diary Password: ")
        if pwd == PASSWORD:
            return True
        attempts -= 1
        print(f"Incorrect. {attempts} attempts left.")
    return False

def add_entry():
    """Adds a date-stamped entry."""
    entry = input("Write your diary entry: ")
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(FILE_NAME, 'a', encoding='utf-8') as file:
        file.write(f"[{date_str}] {entry}\n")
    print("Entry saved.")

def view_entries():
    """Reads all diary entries."""
    if not os.path.exists(FILE_NAME):
        print("Diary is empty.")
        return
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        print("\n--- Diary Entries ---")
        print(file.read())

def search_entries():
    """Searches for a keyword in entries."""
    keyword = input("Enter keyword to search: ").lower()
    if not os.path.exists(FILE_NAME):
        return
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        found = False
        for line in file:
            if keyword in line.lower():
                print(line.strip())
                found = True
        if not found:
            print("No matching entries found.")

def main():
    """Main application loop."""
    if not authenticate():
        print("Access Denied.")
        return
        
    while True:
        print("\n1. Add Entry | 2. View Entries | 3. Search | 4. Lock & Exit")
        choice = input("Choice: ").strip()
        if choice == '1': add_entry()
        elif choice == '2': view_entries()
        elif choice == '3': search_entries()
        elif choice == '4': break

if __name__ == "__main__":
    main()