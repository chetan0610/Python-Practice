"""
Program 8: Default Parameters
Description: Demonstrates the use of default parameter values in functions.
"""

def display_user_profile(user_name, country="India", user_age=18):
    """
    Displays a user's profile using default values if not provided.
    
    Args:
        user_name (str): The name of the user.
        country (str, optional): The user's country. Defaults to "India".
        user_age (int, optional): The user's age. Defaults to 18.
    """
    print(f"Name: {user_name} | Age: {user_age} | Country: {country}")

if __name__ == "__main__":
    print("--- Profile 1 (Defaults used) ---")
    display_user_profile("Aarav")
    
    print("\n--- Profile 2 (Custom country, default age) ---")
    display_user_profile("Sarah", country="Canada")
    
    print("\n--- Profile 3 (All custom values) ---")
    display_user_profile("Kenji", "Japan", 25)