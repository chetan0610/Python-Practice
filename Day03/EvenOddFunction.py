def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


user_num = int(input("Enter a number: "))
result = check_even_odd(user_num)

print(f"The number {user_num} is {result}.")