from cs50 import get_int

while True:
    height = get_int("Height: ") #asks user for height of pyrimad
    if 1 <= height and height <= 8: # Break loop if the height meets requirements
        break

reps = height - 1

for i in range(height):
    print(" " * reps, end ="")
    reps = reps - 1
    s = i + 1
    print("#" * s, end ="")
    print("  ", end ="")
    print("#" * s)
