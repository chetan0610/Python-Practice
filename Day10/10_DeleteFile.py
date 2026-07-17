"""
10_DeleteFile.py
Handles file paths, shows absolute path and extensions, and optionally deletes the file.
"""
import os

def main():
    """Displays path details and allows safe deletion of a file."""
    filepath = input("Enter the file path: ").strip()
    
    if not os.path.exists(filepath):
        print("File does not exist.")
        return
        
    abs_path = os.path.abspath(filepath)
    filename, ext = os.path.splitext(os.path.basename(filepath))
    
    print(f"\n--- Path Information ---")
    print(f"Absolute Path: {abs_path}")
    print(f"Filename: {filename}")
    print(f"Extension: {ext}")
    print("------------------------")
    
    delete = input("Do you want to delete this file? (yes/no): ").strip().lower()
    if delete == 'yes':
        try:
            os.remove(filepath)
            print("File deleted successfully.")
        except PermissionError:
            print("Error: You lack permissions to delete this file.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()