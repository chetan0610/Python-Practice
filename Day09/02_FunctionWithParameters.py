"""
Program 2: Function with Parameters
Description: Accepts a person's name as a parameter and prints a personalized greeting.
"""

def greet_user(user_name):
    """
    Displays a personalized greeting.
    
    Args:
        user_name (str): The name of the user to greet.
    """
    print(f"Hello, {user_name}! I hope you are having a fantastic day.")

if __name__ == "__main__":
    # Challenge: Greet three different users
    print("--- Greeting Multiple Users ---")
    
    user_count = 3
    for current_user in range(user_count):
        name_input = input(f"Enter the name for user {current_user + 1}: ").strip()
        if name_input:
            greet_user(name_input)
        else:
            print("Invalid input. Name cannot be empty.")