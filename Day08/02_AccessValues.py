"""
Program: 02_AccessDictionary.py
Topic: Accessing Dictionary Values
Description: Learn how to access dictionary values using [] and .get() with user inputs.
"""

# ==========================================
# Step 2: Create Student Dictionary via Input
# ==========================================
print("--- Enter Student Details ---")
student = {}
student["id"] = int(input("Enter Student ID (e.g., 101): "))
student["name"] = input("Enter Student Name: ")
student["course"] = input("Enter Course: ")
student["year"] = int(input("Enter Year (e.g., 1): "))
student["college"] = input("Enter College Name: ")

# ==========================================
# Step 3: Print using square brackets []
# ==========================================
print("\n--- Student Details (Using []) ---")
print("Student ID:", student["id"])
print("Student Name:", student["name"])
print("Course:", student["course"])
print("Year:", student["year"])
print("College:", student["college"])

# ==========================================
# Step 4: Print using .get() method
# ==========================================
print("\n--- Using .get() Method ---")
print("Student Name:", student.get("name"))
print("Course:", student.get("course"))

# ==========================================
# Step 5 & 6: Accessing a key that doesn't exist
# ==========================================
print("\n--- Testing Missing Keys ---")
# Without default value (returns None)
print("Phone (without default):", student.get("phone"))

# With default value
print("Phone (with default):", student.get("phone", "Not Available"))
print("\n" + "="*40 + "\n")


# ==========================================
# Bonus Challenge: Interactive Car Dictionary
# ==========================================
print("--- Enter Car Details ---")
car = {}
car["brand"] = input("Enter Car Brand: ")
car["model"] = input("Enter Car Model: ")
car["color"] = input("Enter Color: ")
car["year"] = int(input("Enter Year (e.g., 2023): "))
car["price"] = int(input("Enter Price: "))

print("\n--- Car Details (Using .get()) ---")
print("Brand:", car.get("brand"))
print("Model:", car.get("model"))
print("Color:", car.get("color"))
print("Year:", car.get("year"))
print("Price:", car.get("price"))
print("\n" + "="*40 + "\n")


# ==========================================
# Extra Challenge: Ask user for a key to search
# ==========================================
print("--- Search Student Record ---")
user_key = input("Enter a key to search for in the student dictionary (e.g., name, course, phone): ")

# Using .get() to safely check if the key exists
value = student.get(user_key)

if value is None:
    print("Key not found!")
else:
    print("Value found:")
    print(f"{user_key}: {value}")