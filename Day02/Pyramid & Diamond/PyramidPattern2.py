def print_diamond(n):
    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()

print_diamond(5)