# Program to count digits in a number using while loop

num = int(input("Enter a number: "))
count = 0

# Convert number to positive if negative
if num < 0:
    num = -num

while num != 0:
    num = num // 10
    count = count + 1

print("Total digits:", count)