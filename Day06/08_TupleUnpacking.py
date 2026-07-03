# Demonstrates how to unpack tuple elements into individual variables.
student = ("Rahul", 20, "Python")

name, age, course = student

print("Student Details\n")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Course : {course}")

print("\n--------------------------\n")


product = ("Laptop", 55000, "Dell", "Electronics")

prod_name, price, brand, category = product

print("Product Details\n")
print(f"Name     : {prod_name}")
print(f"Price    : {price}")
print(f"Brand    : {brand}")
print(f"Category : {category}")