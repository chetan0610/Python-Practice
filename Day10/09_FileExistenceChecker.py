"""
09_FileExistenceChecker.py
Checks whether a file exists and creates it if it is missing.
"""
import os

def main():
    """Verifies file existence and safely creates it if absent."""
    filename = input("Enter the filename to check: ").strip()
    
    if os.path.exists(filename):
        print(f"The file '{filename}' already exists.")
    else:
        print(f"The file '{filename}' does not exist.")
        choice = input("Do you want to create it? (y/n): ").strip().lower()
        if choice == 'y':
            try:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write("File automatically generated.\n")
                print(f"File '{filename}' created successfully.")
            except Exception as e:
                print(f"Failed to create file: {e}")

if __name__ == "__main__":
    main()