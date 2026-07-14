"""
Mini Project 2: Student Result System
Description: System to input student marks, calculate total, average, percentage, and assign grades.
Supports multiple students.
"""

def input_marks(subject_count):
    """
    Prompts user for marks in a given number of subjects.
    
    Args:
        subject_count (int): Number of subjects.
        
    Returns:
        list: List of valid numeric marks.
    """
    marks = []
    for i in range(subject_count):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i+1} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return marks

def calculate_total(marks_list):
    """Returns the sum of all marks."""
    return sum(marks_list)

def calculate_average(marks_list):
    """Returns the average of marks."""
    if not marks_list:
        return 0
    return sum(marks_list) / len(marks_list)

def calculate_percentage(total_marks, max_possible_marks):
    """Returns the percentage based on total and max possible."""
    if max_possible_marks == 0:
        return 0
    return (total_marks / max_possible_marks) * 100

def assign_grade(percentage):
    """
    Assigns a letter grade based on percentage.
    
    Args:
        percentage (float): The calculated percentage.
        
    Returns:
        str: Letter grade.
    """
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def display_report(student_name, marks_list):
    """Prints a formatted report card for a student."""
    total = calculate_total(marks_list)
    average = calculate_average(marks_list)
    max_possible = len(marks_list) * 100
    percentage = calculate_percentage(total, max_possible)
    grade = assign_grade(percentage)
    
    print("\n" + "="*30)
    print(f"REPORT CARD: {student_name.upper()}")
    print("="*30)
    print(f"Marks List: {marks_list}")
    print(f"Total Marks: {total} / {max_possible}")
    print(f"Average: {average:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Final Grade: {grade}")
    print("="*30 + "\n")

if __name__ == "__main__":
    # Challenge: Support multiple students
    while True:
        try:
            num_students = int(input("How many students do you want to process? "))
            if num_students > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Enter an integer.")

    num_subjects = 3 # Keeping it fixed to 3 for simplicity, can be dynamic
    
    for student_idx in range(num_students):
        print(f"\n--- Entering details for Student {student_idx + 1} ---")
        name = input("Enter student name: ").strip()
        student_marks = input_marks(num_subjects)
        display_report(name, student_marks)