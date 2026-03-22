Valid= False
while not Valid:
    try:
        n=int(input("enter a number"))
        while n%2==0:

            print("bye")
        Valid=True
    except ValueError:
        print("invalid")


