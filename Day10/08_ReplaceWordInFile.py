"""
08_ReplaceWordInFile.py
Searches for a word in a file and replaces it with a new word, saving the file.
"""

def main():
    """Replaces all instances of a target word with a replacement word in a file."""
    filename = input("Enter the filename: ").strip()
    old_word = input("Enter the word to replace: ").strip()
    new_word = input("Enter the new word: ").strip()
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
        updated_content = content.replace(old_word, new_word)
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(updated_content)
            
        print(f"Successfully replaced '{old_word}' with '{new_word}'.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()