import os

def shutdown_system(choice):
    if choice == "yes":
        print("Shutting down the system...")
        os.system("shutdown /s /t 1")   # For Windows

    elif choice == "no":
        print("Shutdown cancelled.")

    else:
        print("Invalid input! Please enter yes or no.")

# Taking user input
user_choice = input("Do you want to shutdown the computer? (yes/no): ")

# Calling function with argument
shutdown_system(user_choice)