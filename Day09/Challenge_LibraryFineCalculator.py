"""
End of Day Challenge: Library Fine Calculator
Description: Calculates library fines based on overdue days using a menu-driven interface.
Includes multiple functions, input validation, and professional formatting.
"""

def display_library_menu():
    """Prints the main menu for the library fine system."""
    print("\n=== Library Fine Management System ===")
    print("1. Calculate Fine")
    print("2. View Fine Rates")
    print("3. Exit System")
    print("======================================")

def get_valid_integer(prompt):
    """
    Helper function to safely get integer input from the user.
    
    Args:
        prompt (str): The message to display to the user.
        
    Returns:
        int: A valid integer, or -1 if invalid to trigger re-entry.
    """
    try:
        return int(input(prompt))
    except ValueError:
        return -1

def calculate_fine_amount(days_overdue):
    """
    Calculates the fine amount based on business rules.
    
    Rates:
    - 0 days: $0
    - 1 to 5 days: $1.00 per day
    - 6 to 10 days: $2.00 per day
    - 11+ days: $5.00 per day + account suspension warning
    
    Args:
        days_overdue (int): Number of days the book is late.
        
    Returns:
        float: Total fine amount.
    """
    if days_overdue <= 0:
        return 0.0
    elif days_overdue <= 5:
        return days_overdue * 1.0
    elif days_overdue <= 10:
        return days_overdue * 2.0
    else:
        return days_overdue * 5.0

def check_suspension_status(days_overdue):
    """
    Determines if the account should be suspended based on overdue days.
    
    Args:
        days_overdue (int): Number of days late.
        
    Returns:
        bool: True if account should be suspended, False otherwise.
    """
    return days_overdue > 10

def display_fine_rates():
    """Prints the official library fine policy."""
    print("\n--- Current Fine Policy ---")
    print("On Time (0 days)  : No Fine")
    print("1 - 5 days late   : $1.00 per day")
    print("6 - 10 days late  : $2.00 per day")
    print("11+ days late     : $5.00 per day (Account Suspended)")
    print("---------------------------")

def process_return():
    """Handles the user interaction loop for returning a book and calculating fine."""
    days = -1
    while days < 0:
        days = get_valid_integer("Enter number of days overdue (0 if on time): ")
        if days < 0:
            print("Error: Overdue days must be a positive integer or 0.")
            
    fine = calculate_fine_amount(days)
    is_suspended = check_suspension_status(days)
    
    print(f"\n--- Return Receipt ---")
    print(f"Days Overdue: {days}")
    print(f"Total Fine: ${fine:.2f}")
    if is_suspended:
        print("STATUS: ACCOUNT SUSPENDED. Please see librarian.")
    print("----------------------")

if __name__ == "__main__":
    system_running = True
    while system_running:
        display_library_menu()
        user_selection = get_valid_integer("Select an option (1-3): ")
        
        if user_selection == 1:
            process_return()
        elif user_selection == 2:
            display_fine_rates()
        elif user_selection == 3:
            print("Shutting down Library Fine Management System. Goodbye.")
            system_running = False
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")