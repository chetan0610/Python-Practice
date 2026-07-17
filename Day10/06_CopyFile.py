"""
06_CopyFile.py
Copies content from one file to another, allowing the user to copy specific lines.
"""

def main():
    """Reads a source file and writes selected lines to a destination file."""
    source = input("Enter the source filename: ").strip()
    destination = input("Enter the destination filename: ").strip()
    
    try:
        with open(source, 'r', encoding='utf-8') as src_file:
            lines = src_file.readlines()
            
        print(f"The source file has {len(lines)} lines.")
        start = int(input("Enter starting line number to copy (1 for start): "))
        end = int(input(f"Enter ending line number to copy ({len(lines)} for end): "))
        
        # Adjusting for 0-based indexing
        selected_lines = lines[max(0, start - 1):min(len(lines), end)]
        
        with open(destination, 'w', encoding='utf-8') as dest_file:
            dest_file.writelines(selected_lines)
            
        print(f"Successfully copied lines {start} to {end} into '{destination}'.")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except ValueError:
        print("Invalid line numbers entered.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()