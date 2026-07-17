"""
05_CountLinesWordsCharacters.py
Counts lines, words, and characters in a file, specifically ignoring blank lines.
"""

def main():
    """Calculates statistics for a given text file."""
    filename = input("Enter the filename to analyze: ").strip()
    
    lines_count = 0
    words_count = 0
    chars_count = 0
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():  # Ignores blank lines
                    lines_count += 1
                    words_count += len(line.split())
                    chars_count += len(line)
                    
        print(f"\nStatistics for '{filename}':")
        print(f"Valid Lines: {lines_count}")
        print(f"Words: {words_count}")
        print(f"Characters: {chars_count}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()