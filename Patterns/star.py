def print_star_pattern(n):
    for i in range(n):
        for j in range(i + 1):
            print("* ", end="")
        print()
        
    for i in range(n - 1, 0, -1):
        for j in range(i):
            print("* ", end="")
        print()

n = 5  # Specify the number of rows for the star pattern
print_star_pattern(n)
