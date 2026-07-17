"""
12_FileStatistics.py
Writes user data into a CSV file, appending multiple records.
"""
import csv
import os

def main():
    """Collects user data and appends it to a CSV file."""
    filename = input("Enter the CSV filename to save to: ").strip()
    
    file_exists = os.path.exists(filename)
    
    try:
        with open(filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write header if new file
            if not file_exists or os.path.getsize(filename) == 0:
                writer.writerow(['Name', 'Age', 'Department'])
                
            while True:
                name = input("Enter Name (or 'quit' to stop): ").strip()
                if name.lower() == 'quit':
                    break
                age = input("Enter Age: ").strip()
                dept = input("Enter Department: ").strip()
                
                writer.writerow([name, age, dept])
                print("Record added!")
                
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()