def custom_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print("*" * i)

num_rows = 5
custom_pattern(num_rows)