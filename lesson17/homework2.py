import os

def shutdown_system(choice):
    if choice == "yes":
        print("Shutting down the system...")
        os.system("shutdown /s /t 1")   

    elif choice == "no":
        print("Shutdown cancelled.")

    else:
        print("Invalid input! Please enter yes or no.")
user_choice = input("Do you want to shutdown the computer? (yes/no): ")

shutdown_system(user_choice)
shutdown_system(user_choice)