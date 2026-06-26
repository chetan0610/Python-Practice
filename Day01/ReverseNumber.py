# Program to reverse a number using arithmetic operators

try:
    num = int(input("Enter an integer to reverse: "))
    
    # Store the original number for the final print statement
    original_num = num  
    reverse = 0

    # Handle negative numbers by working with the absolute value
    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)

    # While loop to reverse the digits mathematically
    while num > 0:
        # Step 1: Get the last digit
        last_digit = num % 10
        
        # Step 2: Push existing digits left (multiply by 10) and add the new digit
        reverse = (reverse * 10) + last_digit
        
        # Step 3: Remove the last digit from the original number
        num = num // 10

    # If the original number was negative, make the reversed number negative
    if is_negative:
        reverse = -reverse

    print(f"The reverse of {original_num} is: {reverse}")

except ValueError:
    print("Invalid input! Please enter a valid integer.")