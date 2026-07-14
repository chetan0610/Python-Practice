"""
Program 6: Factorial Function
Description: Calculates the factorial of a positive integer using an iterative approach.
"""

def calculate_factorial(number):
    """
    Calculates the factorial of a given non-negative integer.
    
    Args:
        number (int): The number to calculate the factorial for.
        
    Returns:
        int: The factorial of the number.
    """
    if number == 0 or number == 1:
        return 1
        
    factorial_result = 1
    for current_multiplier in range(2, number + 1):
        factorial_result *= current_multiplier
        
    return factorial_result

if __name__ == "__main__":
    try:
        user_input = int(input("Enter a positive integer to find its factorial: "))
        
        # Validation: Don't allow negative numbers
        if user_input < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            result = calculate_factorial(user_input)
            print(f"The factorial of {user_input} is {result}")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")