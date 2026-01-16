height = float(input("enter your height in cm"))
weight = float(input("enter your weight in kg"))
bmi = weight / (height/100)**2
if bmi <= (18.4):
    print("under weight")
elif bmi <= (24.9):
    print("healthy")
elif bmi <= (34.9):
    print("you are over weight") 
else:
    print("obease") 

      
