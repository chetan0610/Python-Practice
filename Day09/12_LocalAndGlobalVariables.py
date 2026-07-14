"""
Program 12: Local and Global Variables
Description: Demonstrates the difference between local and global scope in Python.
"""

# Global variable accessible everywhere in this module
global_system_status = "ONLINE"

def update_system_status():
    """
    Demonstrates local variables and modifying global variables using the global keyword.
    """
    # Local variable only accessible inside this function
    local_process_count = 5
    
    # Challenge: Experiment with the global keyword
    global global_system_status
    print(f"Inside function (before change) - Global Status: {global_system_status}")
    print(f"Inside function - Local Process Count: {local_process_count}")
    
    # Modifying the global variable
    global_system_status = "MAINTENANCE"
    print(f"Inside function (after change) - Global Status: {global_system_status}")

if __name__ == "__main__":
    print(f"Outside function (initial) - Global Status: {global_system_status}")
    
    update_system_status()
    
    print(f"Outside function (final) - Global Status: {global_system_status}")
    
    # Attempting to print local_process_count here would raise a NameError
    # print(local_process_count) # Uncommenting this will crash the program