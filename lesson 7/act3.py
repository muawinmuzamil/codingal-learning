print("enter your marks in 5 subjects")
sub1=int(input("enter your marks"))
sub2=int(input("enter your marks"))
sub3=int(input("enter your marks"))
sub4=int(input("enter your marks"))
avg=(sub1+sub2+sub3+sub4)/4
if avg >=90:
    print("a1")
elif avg >=80:
    print("b")
elif avg >=60:
    print("c")
else:
    print("fail")