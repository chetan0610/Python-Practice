"""
13_MergeTwoFiles.py
Reads data from JSON file and pretty-prints it.
(Note: Matched to Q13 prompt: 'Read data from a JSON file')
"""
import json

def main():
    """Loads a JSON file and pretty-prints the dictionary."""
    filename = input("Enter the JSON filename to read: ").strip()
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
        print("\n--- JSON Data ---")
        print(json.dumps(data, indent=4))
        print("-----------------")
        
    except FileNotFoundError:
        print("Error: File not found.")
    except json.JSONDecodeError:
        print("Error: File is not a valid JSON format.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()