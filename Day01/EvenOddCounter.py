n = int(input("How many numbers do you want to enter? "))

if n <= 0:
    print("Please enter a number greater than 0.")
else:
    even_count = 0
    odd_count = 0

    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))

        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"\nTotal Even numbers: {even_count}")
    print(f"Total Odd numbers: {odd_count}")