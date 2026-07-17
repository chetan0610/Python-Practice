"""
02_ReadFile.py
Reads the entire contents of a text file and displays it with line numbers.
"""

def main():
    """Reads a file and displays its content."""
    filename = input("Enter the filename to read: ").strip()
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.readlines()
            
            if not content:
                print("The file is empty.")
                return
                
            print(f"\n--- Contents of {filename} ---")
            for i, line in enumerate(content, start=1):
                print(f"{i:02d} | {line}", end='')
            print("\n------------------------------")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()