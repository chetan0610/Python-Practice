"""
Program 15: Recursive Fibonacci
Description: Generates the Fibonacci sequence recursively and compares it with iteration.
"""

def get_fibonacci_recursive(term_index):
    """
    Gets the nth Fibonacci number using recursion.
    
    Args:
        term_index (int): The index in the sequence (0-based).
        
    Returns:
        int: The Fibonacci number at that index.
    """
    # Base cases
    if term_index <= 0:
        return 0
    if term_index == 1:
        return 1
        
    # Recursive step
    return get_fibonacci_recursive(term_index - 1) + get_fibonacci_recursive(term_index - 2)

def generate_fibonacci_iterative(terms_count):
    """
    Generates Fibonacci sequence using iteration (for comparison).
    
    Args:
        terms_count (int): Number of terms to generate.
        
    Returns:
        list: The Fibonacci sequence.
    """
    sequence = []
    num_a, num_b = 0, 1
    for _ in range(terms_count):
        sequence.append(num_a)
        num_a, num_b = num_b, num_a + num_b
    return sequence

if __name__ == "__main__":
    try:
        num_terms = int(input("How many Fibonacci terms do you want to generate? "))
        
        if num_terms <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            print("\n--- Recursive Approach ---")
            for i in range(num_terms):
                print(get_fibonacci_recursive(i), end=" ")
            
            print("\n\n--- Iterative Approach (Challenge Comparison) ---")
            iterative_result = generate_fibonacci_iterative(num_terms)
            for val in iterative_result:
                print(val, end=" ")
            print()
            
    except ValueError:
        print("Invalid input. Please enter a positive integer.")