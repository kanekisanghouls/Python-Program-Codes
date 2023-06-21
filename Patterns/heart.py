def print_heart_pattern():
    rows = 6
    for i in range(rows):
        for j in range(100):
            if (i == 0 and j % 8 == 1) or (i == 1 and j % 8 in [0, 2]) or \
                    (i == 2 and j % 8 in [0, 3, 5]) or \
                    (i == 3 and j % 8 in [0, 4, 6, 7]) or \
                    (i == 4 and j % 8 in [1, 3, 5, 7]) or \
                    (i == 5 and j % 8 in [2, 6]):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_heart_pattern()
