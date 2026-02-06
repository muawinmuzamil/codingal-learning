num=int(input("enter a number"))
sum=0
pow=len(str(num))
temp=num
while temp>0:
    digit =temp%10
    sum+=digit**pow
    temp//=10
if num==sum:
    print("armstrong number")
else:
    print("not armstrong number")       