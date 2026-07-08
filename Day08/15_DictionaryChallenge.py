# ==========================================
# Program 15: 15_DictionaryChallenge.py
# Description: Final Practical Exam for Day 08.
# A complete Menu-Driven Dictionary Manager with JSON file persistence.
# ==========================================
import json
import os

# Define the file name where our data will live
FILE_NAME = "dictionary_data.json"

def load_dictionary():
    """Extra Challenge: Load data from JSON file when program starts."""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                print(f"📂 Loaded existing data from {FILE_NAME}")
                return json.load(file)
        except json.JSONDecodeError:
            print("⚠️ File is corrupted or empty. Starting fresh.")
            return {}
    else:
        print("✨ No existing save file found. Starting with an empty dictionary.")
        return {}

def save_dictionary(data):
    """Bonus Challenge: Save data to a JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
    print(f"💾 Dictionary successfully saved to {FILE_NAME}!")

def display_dict(title, data):
    """Helper function for neat output."""
    print(f"\n========== {title} ==========")
    if not data:
        print("{} (Empty)")
    else:
        print(json.dumps(data, indent=4))

def main():
    print("🚀 INITIALIZING DICTIONARY MANAGER...")
    
    # Load data from the file (or start empty)
    my_dict = load_dictionary()

    while True:
        print("\n" + "="*40)
        print("🛠️ DICTIONARY MANAGER 🛠️")
        print("="*40)
        print("1. Create/Reset Dictionary")
        print("2. Display Dictionary")
        print("3. Add Item (setdefault)")
        print("4. Update Item (update)")
        print("5. Remove Item (pop / popitem)")
        print("6. Search Key (get)")
        print("7. Display Keys (keys)")
        print("8. Display Values (values)")
        print("9. Display Items (items)")
        print("10. Clear Dictionary (clear)")
        print("11. Exit & Save")
        print("="*40)
        
        choice = input("Enter your choice (1-11): ").strip()

        if choice == '1':
            print("\n--- Create / Reset Dictionary ---")
            confirm = input("This will erase current data. Are you sure? (yes/no): ").strip().lower()
            if confirm == 'yes':
                # Creating a default template and using .copy() to fulfill the requirement
                template = {"status": "initialized", "user": "admin"}
                my_dict = template.copy()
                print("✅ Dictionary reset to default template!")

        elif choice == '2':
            display_dict("CURRENT DICTIONARY", my_dict)

        elif choice == '3':
            print("\n--- Add Item ---")
            key = input("Enter new key: ").strip()
            val = input("Enter value: ").strip()
            
            # setdefault() only adds the item if the key DOES NOT already exist
            existing_val = my_dict.setdefault(key, val)
            if existing_val == val:
                print(f"✅ Added {key}: {val}")
            else:
                print(f"⚠️ Key '{key}' already exists with value '{existing_val}'. Use Update (Option 4) to change it.")

        elif choice == '4':
            print("\n--- Update Item ---")
            key = input("Enter key to update: ").strip()
            val = input("Enter new value: ").strip()
            
            # update() overwrites existing keys or creates them if they don't exist
            my_dict.update({key: val})
            print(f"✅ Updated {key} to {val}")

        elif choice == '5':
            print("\n--- Remove Item ---")
            sub_choice = input("Type '1' to remove a specific key (pop) or '2' to remove the last item (popitem): ").strip()
            
            if sub_choice == '1':
                key = input("Enter key to remove: ").strip()
                if key in my_dict:
                    removed = my_dict.pop(key)
                    print(f"✅ Removed key '{key}' with value '{removed}'")
                else:
                    print("❌ Key not found!")
            elif sub_choice == '2':
                if my_dict:
                    removed_item = my_dict.popitem()
                    print(f"✅ Removed last inserted item: {removed_item}")
                else:
                    print("❌ Dictionary is already empty!")
            else:
                print("❌ Invalid sub-choice.")

        elif choice == '6':
            print("\n--- Search Key ---")
            key = input("Enter key to search: ").strip()
            
            # get() safely retrieves data without throwing a KeyError
            result = my_dict.get(key, "❌ Key not found!")
            print(f"Result: {result}")

        elif choice == '7':
            print("\n--- Display Keys ---")
            print(list(my_dict.keys()))

        elif choice == '8':
            print("\n--- Display Values ---")
            print(list(my_dict.values()))

        elif choice == '9':
            print("\n--- Display Items ---")
            for k, v in my_dict.items():
                print(f"Key: {k} | Value: {v}")

        elif choice == '10':
            print("\n--- Clear Dictionary ---")
            confirm = input("Are you sure you want to delete everything? (yes/no): ").strip().lower()
            if confirm == 'yes':
                my_dict.clear()
                print("✅ Dictionary cleared!")

        elif choice == '11':
            print("\nInitiating shutdown sequence...")
            save_dictionary(my_dict)
            print("Exiting Dictionary Manager. You crushed Day 08! 🚀")
            break

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 11.")

if __name__ == "__main__":
    main()
    