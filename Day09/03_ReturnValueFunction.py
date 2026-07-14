"""
Program 3: Function Returning Value
Description: Calculates the sum of two numbers and returns the result to be used later.
"""

def calculate_sum(number_one, number_two):
    """
    Calculates and returns the sum of two numbers.
    
    Args:
        number_one (float): The first number.
        number_two (float): The second number.
        
    Returns:
        float: The sum of the two numbers.
    """
    return number_one + number_two

if __name__ == "__main__":
    try:
        first_input = float(input("Enter the first number: "))
        second_input = float(input("Enter the second number: "))
        
        # Process: Return result and print outside
        total_sum = calculate_sum(first_input, second_input)
        print(f"The sum is: {total_sum}")
        
        # Challenge: Use the returned value in another calculation
        multiplied_result = total_sum * 10
        print(f"The sum multiplied by 10 is: {multiplied_result}")
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")