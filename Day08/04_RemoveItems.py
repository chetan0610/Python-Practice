# ==========================================
# Program 04 Pro: 04_RemoveItems_Pro.py
# Description: Demonstrating dictionary data removal
# with professional input validation and outputs.
# ==========================================
import json

def display_dict(title, data_dict):
    print(f"\n========== {title} ==========")
    print(json.dumps(data_dict, indent=4))

def main():
    # Pre-filling the dictionary for testing speed
    student = {
        "id": 101,
        "name": "Chetan",
        "course": "ECE",
        "year": 1,
        "college": "SMEC",
        "phone": "9876543210",
        "email": "abc@gmail.com"
    }

    display_dict("ORIGINAL", student)

    # --- Remove with pop() ---
    key_to_pop = input("\nEnter key to remove using pop():\n").strip()
    if key_to_pop in student:
        removed_value = student.pop(key_to_pop)
        print(f"\nRemoved Value:\n{removed_value}")
        display_dict("AFTER POP", student)
    else:
        print("\nKey not found!")

    # --- Remove with popitem() ---
    # Improvement 2: Input Validation Loop
    while True:
        remove_last = input("\nRemove last inserted item? (yes/no)\n").strip().lower()
        if remove_last in ("yes", "no"):
            break
        print("Invalid input. Please enter 'yes' or 'no'.")

    if remove_last == 'yes':
        if student:
            # Improvement 1: Show the Tuple
            removed_item = student.popitem()
            print(f"\nRemoved Item:\n{removed_item}")
            display_dict("AFTER POPITEM", student)
        else:
            print("\nDictionary is already empty!")

    # --- Remove with del ---
    key_to_del = input("\nEnter key to delete using del:\n").strip()
    if key_to_del in student:
        del student[key_to_del]
        display_dict("AFTER DEL", student)
    else:
        print("\nKey not found!")

    # --- clear() ---
    while True:
        clear_dict = input("\nClear dictionary? (yes/no)\n").strip().lower()
        if clear_dict in ("yes", "no"):
            break
        print("Invalid input. Please enter 'yes' or 'no'.")

    if clear_dict == 'yes':
        student.clear()
        display_dict("FINAL", student)

    # Improvement 3: Goodbye Message
    print("\nProgram Completed Successfully! 🚀")

if __name__ == "__main__":
    main()