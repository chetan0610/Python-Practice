"""
Program 10: Variable-Length Arguments (*args)
Description: Accepts an unlimited number of integers to calculate their sum and average.
"""

def calculate_sum_and_average(*numbers):
    """
    Calculates the total and average of a variable number of integers.
    
    Args:
        *numbers (float/int): An arbitrary number of numeric arguments.
        
    Returns:
        tuple: A tuple containing (total_sum, average). Returns (0, 0) if empty.
    """
    if not numbers:
        return 0, 0
        
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    
    return total_sum, average

if __name__ == "__main__":
    print("--- Test 1: Three numbers ---")
    total, avg = calculate_sum_and_average(10, 20, 30)
    print(f"Total: {total}, Average: {avg:.2f}")
    
    print("\n--- Test 2: Seven numbers ---")
    total, avg = calculate_sum_and_average(5, 15, 25, 35, 45, 55, 65)
    print(f"Total: {total}, Average: {avg:.2f}")
    
    print("\n--- Test 3: No numbers ---")
    total, avg = calculate_sum_and_average()
    print(f"Total: {total}, Average: {avg:.2f}")