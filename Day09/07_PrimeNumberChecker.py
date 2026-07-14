"""
Program 7: Prime Number Checker
Description: Checks whether a number is prime and prints prime numbers within a range.
"""
import math

def is_prime(number):
    """
    Checks if a number is prime.
    
    Args:
        number (int): The number to check.
        
    Returns:
        bool: True if prime, False otherwise.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
        
    # Optimization: Check up to the square root of the number
    limit = int(math.sqrt(number)) + 1
    for divisor in range(3, limit, 2):
        if number % divisor == 0:
            return False
            
    return True

if __name__ == "__main__":
    # Challenge: Print all prime numbers within a range
    try:
        start_range = int(input("Enter the start of the range: "))
        end_range = int(input("Enter the end of the range: "))
        
        if start_range > end_range:
            print("Invalid range. Start must be less than or equal to end.")
        else:
            print(f"\nPrime numbers between {start_range} and {end_range}:")
            primes_found = False
            for current_num in range(start_range, end_range + 1):
                if is_prime(current_num):
                    print(current_num, end=" ")
                    primes_found = True
            
            if not primes_found:
                print("No prime numbers found in this range.")
            print() # Print newline
            
    except ValueError:
        print("Invalid input. Please enter valid integers.")