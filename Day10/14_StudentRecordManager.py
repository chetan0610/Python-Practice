"""
14_StudentRecordManager.py
Writes Python dictionary into a JSON file holding multiple student records.
"""
import json
import os

def main():
    """Collects multiple records in a dictionary and saves them to JSON."""
    filename = input("Enter JSON filename to save records: ").strip()
    records = {}
    
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                records = json.load(file)
        except json.JSONDecodeError:
            records = {}

    try:
        while True:
            student_id = input("Enter Student ID (or 'quit' to stop): ").strip()
            if student_id.lower() == 'quit':
                break
                
            name = input("Enter Student Name: ").strip()
            grade = input("Enter Grade: ").strip()
            
            records[student_id] = {"Name": name, "Grade": grade}
            
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(records, file, indent=4)
            
        print("Records saved to JSON successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()