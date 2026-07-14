"""
Program 13: Lambda Functions
Description: Demonstrates simple, anonymous lambda functions for basic math operations.
"""

# Process: Create lambdas for square, addition, and multiplication
calculate_square = lambda x: x ** 2
calculate_addition = lambda x, y: x + y
calculate_multiplication = lambda x, y: x * y

if __name__ == "__main__":
    try:
        base_number = float(input("Enter a number to square: "))
        print(f"Square of {base_number}: {calculate_square(base_number)}")
        
        num1 = float(input("\nEnter first number for math operations: "))
        num2 = float(input("Enter second number for math operations: "))
        
        # Challenge: Execute lambdas for addition and multiplication
        print(f"Addition ({num1} + {num2}): {calculate_addition(num1, num2)}")
        print(f"Multiplication ({num1} * {num2}): {calculate_multiplication(num1, num2)}")
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")