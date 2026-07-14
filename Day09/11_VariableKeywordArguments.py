"""
Program 11: Variable-Length Keyword Arguments (**kwargs)
Description: Uses **kwargs to print dynamically provided student details.
"""

def display_student_details(**student_data):
    """
    Displays dynamically provided student information.
    
    Args:
        **student_data (str/int): Arbitrary keyword arguments representing student details.
    """
    if not student_data:
        print("No student data provided.")
        return
        
    print("-" * 30)
    # Process: Loop through the dictionary and format neatly
    for key, value in student_data.items():
        # Formatting key to look like a title (e.g., first_name -> First Name)
        formatted_key = str(key).replace("_", " ").title()
        print(f"{formatted_key:<15}: {value}")
    print("-" * 30)

if __name__ == "__main__":
    print("Student 1:")
    display_student_details(name="Alice Smith", grade="A", age=20, major="Computer Science")
    
    print("\nStudent 2:")
    display_student_details(name="Bob Johnson", graduation_year=2025, gpa=3.8, extracurriculars="Robotics Club")