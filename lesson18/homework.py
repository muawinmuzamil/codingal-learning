def check_age():
    try:
        age = int(input("Enter your age: "))

        # Check if age is valid
        if age <= 0:
            print("Invalid age! Age must be greater than 0.")
        else:
            print("Valid age entered.")

            # Check even or odd
            if age % 2 == 0:
                print("The age is Even.")
            else:
                print("The age is Odd.")

    except ValueError:
        print("Error! Please enter a valid number.")

# Call the function
check_age()