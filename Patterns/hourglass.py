def print_hourglass_pattern(n):
    for i in range(n, 0, -1):
        print((n - i) * " ", end="")
        print(i * "* ")
    
    for i in range(2, n+1):
        print((n - i) * " ", end="")
        print(i * "* ")

n = 5  # Specify the number of rows for the hourglass pattern
print_hourglass_pattern(n)
