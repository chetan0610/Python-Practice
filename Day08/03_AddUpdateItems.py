"""
Program: 03_AddUpdateitems.py
Topic: Modifying Dictionaries (Fully Interactive)
Description: Learn how to add, update, and check keys using your own inputs.
"""
import json

# Helper function to print dictionaries neatly on multiple lines
def pretty_print(title, dictionary_data):
    print(f"\n--- {title} ---")
    print(json.dumps(dictionary_data, indent=4))
    print("-" * 40 + "\n")

# ==========================================
# Main Task: Modifying Student Dictionary
# ==========================================
print("=== INITIAL STUDENT SETUP ===")
student = {}
student["id"] = int(input("Enter Student ID (e.g., 101): "))
student["name"] = input("Enter Student Name: ")

pretty_print("Original Dictionary", student)

print("=== ADD NEW ITEMS ===")
student["course"] = input("Enter Course to add: ")
student["year"] = int(input("Enter Year to add (e.g., 1): "))
student["college"] = input("Enter College to add: ")

pretty_print("After Adding New Items", student)

print("=== UPDATE EXISTING VALUES ===")
print("(Let's update the Name and Year)")
student["name"] = input("Enter Updated Name: ")
student["year"] = int(input("Enter Updated Year: "))

pretty_print("After Updating Values", student)

print("=== USE UPDATE() METHOD ===")
phone_input = input("Enter Phone Number to add: ")
email_input = input("Enter Email to add: ")

# Using update() to add multiple items at once
student.update({
    "phone": phone_input,
    "email": email_input
})

pretty_print("After update() Method", student)


# ==========================================
# Bonus Challenge: Mobile Dictionary
# ==========================================
print("=== BONUS CHALLENGE: MOBILE DICTIONARY ===")
mobile = {}
mobile["brand"] = input("Enter Mobile Brand: ")
mobile["model"] = input("Enter Mobile Model: ")
pretty_print("Mobile: Initial Setup", mobile)

mobile["ram"] = input("Enter RAM to add (e.g., 8GB): ")
pretty_print("Mobile: Added RAM", mobile)

mobile["storage"] = input("Enter Storage to add (e.g., 128GB): ")
pretty_print("Mobile: Added Storage", mobile)

print("(Oh wait, let's upgrade the storage!)")
mobile["storage"] = input("Enter Updated Storage (e.g., 256GB): ")
pretty_print("Mobile: Updated Storage", mobile)

price_input = int(input("Enter Price to add: "))
mobile.update({"price": price_input})
pretty_print("Mobile: Added Price via update()", mobile)


# ==========================================
# Extra Challenge: Check if Key Exists
# ==========================================
print("=== EXTRA CHALLENGE: SAFE ADDITION ===")
new_key = input("Enter a key you want to add to the student dictionary: ")

# Check if the key already exists to prevent accidental overwrites
if new_key in student:
    print("\nKey already exists! We won't overwrite it.")
else:
    new_value = input(f"Enter a value for '{new_key}': ")
    
    # Check if the user entered a number so we save it as an integer, otherwise string
    if new_value.isdigit():
        student[new_key] = int(new_value)
    else:
        student[new_key] = new_value

    print("\n Successfully added!")

pretty_print("Final Aff Updated items", student)