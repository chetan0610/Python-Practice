"""
Program 14: Recursive Factorial
Description: Calculates the factorial of a number using recursion, printing intermediate steps.
"""

def recursive_factorial(number):
    """
    Calculates factorial recursively.
    
    Args:
        number (int): The number to calculate factorial for.
        
    Returns:
        int: The factorial of the number.
    """
    # Challenge: Print recursion steps
    print(f"Calculating factorial({number})...")
    
    # Base case
    if number == 0 or number == 1:
        print(f"Base case reached for {number}. Returning 1.")
        return 1
        
    # Recursive step
    result = number * recursive_factorial(number - 1)
    print(f"Returning {number} * factorial({number - 1}) = {result}")
    return result

if __name__ == "__main__":
    try:
        target_number = int(input("Enter a small positive integer (e.g., 5): "))
        if target_number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            final_result = recursive_factorial(target_number)
            print(f"\nFinal Result: The factorial of {target_number} is {final_result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")