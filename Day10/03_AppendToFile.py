"""
03_AppendToFile.py
Appends new content to an existing file along with the current timestamp.
"""
from datetime import datetime

def main():
    """Appends user text to a file without deleting old content."""
    filename = input("Enter the filename to append to: ").strip()
    text = input("Enter the text to append: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"[{timestamp}] {text}\n")
        print("Content appended successfully!")
    except PermissionError:
        print(f"Error: You do not have permission to modify '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()