import math

def print_circle_pattern(radius):
    for i in range(-radius, radius+1):
        for j in range(-radius, radius+1):
            distance = math.sqrt(i**2 + j**2)
            if distance <= radius:
                print("*", end="")
            else:
                print(" ", end="")
        print()

radius = 5  # Specify the radius of the circle
print_circle_pattern(radius)
