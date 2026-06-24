# Insert the number you want to factorial 
num = int(input("Enter the number which you want to find the factorial: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i 

    print(factorial)