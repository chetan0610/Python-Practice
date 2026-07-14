"""
Program 1: Simple Function
Description: Demonstrates a basic function without parameters that prints a welcome message.
Includes a loop to fulfill the challenge requirement.
"""

def display_welcome_message():
    """Prints a two-line welcome message."""
    print("Welcome to our Python learning journey!")
    print("We are excited to have you here.")

if __name__ == "__main__":
    # Challenge: Call the function 5 times using a loop
    print("--- Executing Welcome Function 5 Times ---")
    for iteration in range(5):
        print(f"\nCall {iteration + 1}:")
        display_welcome_message()