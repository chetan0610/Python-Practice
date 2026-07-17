"""
04_ReadLineByLine.py
Reads a file line by line using a loop to manage memory efficiently.
"""

def main():
    """Iterates through a file object directly to print each line."""
    filename = input("Enter the filename to read: ").strip()
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line_num = 1
            print(f"\n--- Reading {filename} Line by Line ---")
            for line in file:
                print(f"Line {line_num}: {line}", end='')
                line_num += 1
            print("\n---------------------------------------")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()