"""
07_SearchWordInFile.py
Searches for a specific word inside a text file (case-insensitive).
"""

def main():
    """Finds and counts all occurrences of a word in a file."""
    filename = input("Enter the filename to search in: ").strip()
    target = input("Enter the word to search for: ").strip().lower()
    
    try:
        occurrences = 0
        with open(filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, start=1):
                words = [w.lower() for w in line.split()]
                count_in_line = words.count(target)
                
                if count_in_line > 0:
                    print(f"Line {line_num}: {line.strip()}")
                    occurrences += count_in_line
                    
        print(f"\nTotal occurrences of '{target}': {occurrences}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()