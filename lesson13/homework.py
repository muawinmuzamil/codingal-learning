rows = int(input("Enter number of rows: "))

i = 1
while i <= rows:
    spaces = rows - i
    stars = 1

    # Print spaces
    while spaces > 0:
        print(" ", end="")
        spaces -= 1

    # Print stars
    while stars <= i:
        print("*", end="")
        stars += 1

    print()  # Move to next line
    i += 1