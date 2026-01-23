a=3
b=5
c=2
avg=(a+b+c)/3
if avg> a and avg> b and avg> c:
    print("avg above all")
elif avg>a and avg>b: 
 print("avg  is above a,b")
elif avg>a and avg> c :
  print("avg is above a,c")
elif avg>b and avg>c:
  print("avg above b,c")
else:
  print("not valid")  