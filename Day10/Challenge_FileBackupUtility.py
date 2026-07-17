"""
Challenge_FileBackupUtility.py
File Organizer: Moves Images, PDFs, Videos, and Documents into respective folders.
"""
import os
import shutil

def main():
    """Scans a directory and organizes files by extension."""
    target_dir = input("Enter directory path to organize: ").strip()
    
    if not os.path.exists(target_dir):
        print("Directory does not exist.")
        return

    # Define categories
    categories = {
        "Images": ['.jpg', '.png', '.jpeg', '.gif'],
        "PDFs": ['.pdf'],
        "Videos": ['.mp4', '.mkv', '.avi'],
        "Documents": ['.docx', '.txt', '.csv', '.xlsx']
    }

    try:
        moved = 0
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            
            if os.path.isdir(item_path):
                continue
                
            ext = os.path.splitext(item)[1].lower()
            
            # Find category for file
            for folder, extensions in categories.items():
                if ext in extensions:
                    folder_path = os.path.join(target_dir, folder)
                    
                    # Create folder automatically if it doesn't exist
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                        
                    shutil.move(item_path, os.path.join(folder_path, item))
                    print(f"Moved {item} -> {folder}/")
                    moved += 1
                    break
                    
        print(f"Organized {moved} files successfully.")
    except Exception as e:
        print(f"Error organizing files: {e}")

if __name__ == "__main__":
    main()