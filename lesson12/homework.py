# Binary to Decimal
binary = int(input("Enter a binary number: "))
original_binary = binary
decimal = 0
power = 0

while binary > 0:
    digit = binary % 10
    decimal = decimal + digit * (2 ** power)
    power += 1
    binary = binary // 10

print("Decimal of", original_binary, "is:", decimal)


# Decimal to Binary
decimal_num = int(input("\nEnter a decimal number: "))
original_decimal = decimal_num
binary_result = ""

while decimal_num > 0:
    remainder = decimal_num % 2
    binary_result = str(remainder) + binary_result
    decimal_num = decimal_num // 2

print("Binary of", original_decimal, "is:", binary_result)
