rows = int(input("enter the num of rows:"))
num=1
print("Flyoids triangle")
for i in range (rows+1):
    for j in range(i):
        print(num,end='')
        num+=1
    print()