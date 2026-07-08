"""
Program: 01_CreateDictionary_Interactive.py
Topic: Dictionaries with User Input
Description: Create and display dictionaries based on user input.
"""

# ==========================================
# Main Task: Interactive Student Dictionary
# ==========================================
print("--- Enter Student Details ---")
student = {} # Create an empty dictionary

# Ask the user for input and store it in the dictionary
student["id"] = int(input("Enter Student ID (e.g., 101): "))
student["name"] = input("Enter Student Name: ")
student["course"] = input("Enter Course: ")
student["year"] = int(input("Enter Year (e.g., 1): "))
student["college"] = input("Enter College Name: ")

print("\n--- Saved Student Record ---")
print(student)
print("\n" + "="*40 + "\n") # Visual separator


# ==========================================
# Bonus Challenge: Interactive Mobile Dictionary
# ==========================================
print("--- Enter Mobile Details ---")
mobile = {}

mobile["brand"] = input("Enter Mobile Brand: ")
mobile["model"] = input("Enter Mobile Model: ")
mobile["ram"] = input("Enter RAM (e.g., 8GB): ")
mobile["storage"] = input("Enter Storage (e.g., 256GB): ")
mobile["price"] = int(input("Enter Price: "))

print("\n--- Saved Mobile Details ---")
print(mobile)
print("\n" + "="*40 + "\n")


# ==========================================
# Extra Challenge: Interactive Laptop Dictionary
# ==========================================
print("--- Enter Laptop Details ---")
laptop = {}

laptop["brand"] = input("Enter Laptop Brand: ")
laptop["processor"] = input("Enter Processor: ")
laptop["ram"] = input("Enter RAM (e.g., 16GB): ")
laptop["ssd"] = input("Enter SSD (e.g., 512GB): ")
laptop["price"] = int(input("Enter Price: "))

print("\n--- Saved Laptop Details ---")
print(laptop)