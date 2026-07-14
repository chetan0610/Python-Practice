"""
Program 4: Even or Odd
Description: Checks whether a given integer is even or odd and returns a string result.
"""

def check_even_odd(number):
    """
    Determines if a number is even or odd.
    
    Args:
        number (int): The number to check.
        
    Returns:
        str: "Even" if the number is even, "Odd" otherwise.
    """
    if number % 2 == 0:
        return "Even"
    return "Odd"

if __name__ == "__main__":
    # Challenge: Check five numbers using a loop
    print("--- Checking 5 Numbers ---")
    iterations = 5
    
    while iterations > 0:
        try:
            user_number = int(input("Enter an integer to check: "))
            result = check_even_odd(user_number)
            print(f"The number {user_number} is {result}.")
            iterations -= 1
        except ValueError:
            print("Invalid input. Please enter a valid integer.")