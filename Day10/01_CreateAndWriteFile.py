"""
01_CreateAndWriteFile.py
Creates a text file and writes multiple lines based on user input.
"""

def create_and_write_file():
    """Asks the user for the number of lines and writes them to a file."""
    filename = input("Enter the filename to create (e.g., data.txt): ").strip()
    if not filename:
        print("Filename cannot be empty.")
        return

    try:
        num_lines = int(input("How many lines do you want to write? "))
        if num_lines <= 0:
            print("Please enter a number greater than 0.")
            return

        with open(filename, 'w', encoding='utf-8') as file:
            for i in range(num_lines):
                line_content = input(f"Enter line {i + 1}: ")
                file.write(line_content + '\n')
                
        print(f"Successfully created '{filename}' and wrote {num_lines} lines.")
        
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    create_and_write_file()