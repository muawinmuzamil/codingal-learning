char = input("Enter a character: ")

# Check uppercase using character comparison
if char >= 'A' and char <= 'Z':
    print("Uppercase letter")

# Check lowercase
elif char >= 'a' and char <= 'z':
    print("Lowercase letter")

# Check digit
elif char >= '0' and char <= '9':
    print("Digit")

# Otherwise special character
else:
    print("Special character")
