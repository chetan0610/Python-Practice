"""
Mini Project 1: Calculator Using Functions
Description: A menu-driven calculator supporting basic arithmetic operations continuously.
"""

def add(num_a, num_b):
    """Returns addition of two numbers."""
    return num_a + num_b

def subtract(num_a, num_b):
    """Returns subtraction of two numbers."""
    return num_a - num_b

def multiply(num_a, num_b):
    """Returns multiplication of two numbers."""
    return num_a * num_b

def divide(num_a, num_b):
    """Returns division, handling division by zero."""
    if num_b == 0:
        return "Error: Cannot divide by zero."
    return num_a / num_b

def modulus(num_a, num_b):
    """Returns modulus, handling division by zero."""
    if num_b == 0:
        return "Error: Cannot divide by zero."
    return num_a % num_b

def power(base, exponent):
    """Returns base raised to exponent."""
    return base ** exponent

def display_menu():
    """Displays the calculator menu options."""
    print("\n--- Python Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

if __name__ == "__main__":
    # Challenge: Continuous calculation until exit
    while True:
        display_menu()
        user_choice = input("Select operation (1-7): ").strip()
        
        if user_choice == '7':
            print("Exiting calculator. Goodbye!")
            break
            
        if user_choice not in ('1', '2', '3', '4', '5', '6'):
            print("Invalid selection. Please try again.")
            continue
            
        try:
            val_one = float(input("Enter first number: "))
            val_two = float(input("Enter second number: "))
            
            if user_choice == '1':
                print(f"Result: {add(val_one, val_two)}")
            elif user_choice == '2':
                print(f"Result: {subtract(val_one, val_two)}")
            elif user_choice == '3':
                print(f"Result: {multiply(val_one, val_two)}")
            elif user_choice == '4':
                print(f"Result: {divide(val_one, val_two)}")
            elif user_choice == '5':
                print(f"Result: {modulus(val_one, val_two)}")
            elif user_choice == '6':
                print(f"Result: {power(val_one, val_two)}")
                
        except ValueError:
            print("Invalid input! Please enter numeric values only.")