"""
Program 5: Largest of Three Numbers
Description: Accepts three numbers, compares them, and returns the largest value.
"""

def find_largest(num_one, num_two, num_three):
    """
    Finds the largest among three numbers.
    
    Args:
        num_one (float): First number.
        num_two (float): Second number.
        num_three (float): Third number.
        
    Returns:
        float: The largest of the three numbers.
    """
    # Handling equal values naturally by using >= in standard max logic
    largest = num_one
    if num_two >= largest:
        largest = num_two
    if num_three >= largest:
        largest = num_three
        
    return largest

if __name__ == "__main__":
    # Challenge: Allow the user to repeat the program
    continue_program = True
    while continue_program:
        try:
            val1 = float(input("\nEnter first number: "))
            val2 = float(input("Enter second number: "))
            val3 = float(input("Enter third number: "))
            
            largest_value = find_largest(val1, val2, val3)
            print(f"The largest number is: {largest_value}")
            
            choice = input("Do you want to check another set? (yes/no): ").strip().lower()
            if choice != 'yes' and choice != 'y':
                continue_program = False
                
        except ValueError:
            print("Invalid input. Please enter numeric values.")