a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Before swapping:", a, b, c)

temp = a
a = b
b = c
c = temp

print("After swapping:", a, b, c)
