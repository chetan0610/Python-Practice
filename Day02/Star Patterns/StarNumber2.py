def custom_pattern(rows):
    for i in range(rows, 0, -1):
        for j in range(i, 0, -1):
            print(j, end="")
        print("*" * i)

num_rows = 5
custom_pattern(num_rows)