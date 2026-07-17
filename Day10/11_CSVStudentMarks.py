"""
11_CSVStudentMarks.py
Reads data from a CSV file, displays it neatly, and counts the records.
"""
import csv

def main():
    """Reads a CSV file and neatly prints its contents."""
    filename = input("Enter the CSV filename to read: ").strip()
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            
            if header:
                print(f"\n{header[0]:<15} | {header[1]:<10} | {header[2]:<10}")
                print("-" * 45)
                
            count = 0
            for row in reader:
                # Assuming 3 columns for safe unpacking, adjust dynamically if needed
                print(f"{row[0]:<15} | {row[1]:<10} | {row[2]:<10}")
                count += 1
                
            print(f"\nTotal Records: {count}")
    except FileNotFoundError:
        print("Error: CSV file not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()