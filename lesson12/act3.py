num=input("enter a value:")
if len(num)>=4:
    mid = len(num)// 2
    midOne = int(num[mid])
    midTwo = int(num[mid-1])
    print(midOne * midTwo)
else:
    print("it is not a four or more than 4 digit number!")  