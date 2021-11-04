
floor = 0

with open ("input.txt", "r") as f:
    for char in f.read():

        if char == "(":
            floor += 1

        elif char == ")":
            floor -= 1

print(floor)
